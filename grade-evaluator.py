import csv
import sys
import os

def load_csv_data():
    """
    Prompts the user for a filename, checks if it exists, 
    and extracts all fields into a list of dictionaries.
    """
    filename = input("Enter the name of the CSV file to process (e.g., grades.csv): ")
    
    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' was not found.")
        sys.exit(1)
        
    assignments = []
    
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Convert numeric fields to floats for calculations
                assignments.append({
                    'assignment': row['assignment'],
                    'group': row['group'],
                    'score': float(row['score']),
                    'weight': float(row['weight'])
                })
        return assignments
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        sys.exit(1)

def evaluate_grades(data):
    """
    Evaluates student grades from a list of assignment dictionaries.
    Validates scores and weights, calculates GPA, determines pass/fail
    status, and identifies assignments eligible for resubmission.
    """
    # Handle empty CSV file gracefully
    if not data:
        print("No assignment data found. The file may be empty.")
        return

    print("\n========== GRADE EVALUATION REPORT ==========\n")

    # a) Score Validation: Ensure all scores fall within the 0-100 range
    print("--- Score Validation ---")
    scores_valid = True
    for item in data:
        if item['score'] < 0 or item['score'] > 100:
            print(f"  [WARNING] Invalid score for '{item['assignment']}': {item['score']} (must be 0-100)")
            scores_valid = False
    if scores_valid:
        print("  All scores are valid.")

    # b) Weight Validation: Total must be 100, Formative must be 60, Summative must be 40
    print("\n--- Weight Validation ---")
    formative_weight = 0
    summative_weight = 0
    total_weight = 0
    # Accumulate weights for each category separately
    for item in data:
        total_weight += item['weight']
        if item['group'] == "Formative":
            formative_weight += item['weight']
        if item['group'] == "Summative":
            summative_weight += item['weight']

    weights_valid = True
    if total_weight != 100:
        print(f"  [WARNING] Total weight is {total_weight}, expected 100.")
        weights_valid = False
    if formative_weight != 60:
        print(f"  [WARNING] Formative weight is {formative_weight}, expected 60.")
        weights_valid = False
    if summative_weight != 40:
        print(f"  [WARNING] Summative weight is {summative_weight}, expected 40.")
        weights_valid = False
    if weights_valid:
        print("  All weights are valid.")

    # c) Calculate Final Grade and GPA
    print("\n--- Grade Calculation ---")
    final_grade = 0
    for item in data:
        # Each assignment contributes (score * weight / 100) to the final grade
        grade = item['score'] * item['weight'] / 100
        final_grade += grade
    # Convert final grade to a GPA on a 5.0 scale
    gpa = (final_grade / 100) * 5.0
    print(f"  Final Grade: {final_grade:.2f}%")
    print(f"  GPA: {gpa:.2f} / 5.00")

    # d) Pass/Fail Status: Student must score >= 50% in BOTH categories
    print("\n--- Pass/Fail Status ---")
    cumulative_formative = 0
    cumulative_summative = 0
    for item in data:
        if item['group'] == "Formative":
            cumulative_formative += item['score'] * item['weight']
        if item['group'] == "Summative":
            cumulative_summative += item['score'] * item['weight']
    # Weighted average per category = total weighted score / total weight for that category
    av_formative = cumulative_formative / formative_weight
    av_summative = cumulative_summative / summative_weight

    print(f"  Formative Average:  {av_formative:.2f}%")
    print(f"  Summative Average:  {av_summative:.2f}%")

    if av_formative >= 50 and av_summative >= 50:
        status = "PASSED"
    else:
        status = "FAILED"
    print(f"\n  >> Final Status: {status}")

    # e) Resubmission Logic: Find failed formative assignments with the highest weight
    print("\n--- Resubmission Eligibility ---")
    failed = []
    highest_weight = 0

    # Step 1: Collect all formative assignments that scored below 50
    for item in data:
        if item['group'] == 'Formative' and item['score'] < 50:
            failed.append(item)

    # Step 2: Find the highest weight among the failed assignments
    for ass in failed:
        if ass['weight'] > highest_weight:
            highest_weight = ass['weight']

    # Step 3: Display all failed assignments that match the highest weight
    resubmit = False
    for ass in failed:
        if ass['weight'] == highest_weight:
            print(f"  Eligible for resubmission: {ass['assignment']} (Score: {ass['score']}%, Weight: {ass['weight']}%)")
            resubmit = True
    if not resubmit:
        print("  No resubmissions needed.")

    print("\n==============================================")

if __name__ == "__main__":
    # 1. Load the data
    course_data = load_csv_data()
    
    # 2. Process the features
    evaluate_grades(course_data)