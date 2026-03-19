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
    Implement your logic here.
    'data' is a list of dictionaries containing the assignment records.
    """
    print("\n--- Processing Grades ---")
    
    # TODO: a) Check if all scores are percentage based (0-100)
    for item in data:
        if item['score'] <0 or item['score'] > 100:
            print(f"Warning! there is a problem with the scores of {item['assignment']}")

    # TODO: b) Validate total weights (Total=100, Summative=40, Formative=60)
    formative_weight = 0
    summative_weight = 0
    total_weight = 0
    for item in data:
        total_weight += item['weight']
        if item['group'] == "Formative":
            formative_weight += item['weight']
        if item['group'] == "Summative":
            summative_weight += item['weight']
    if total_weight != 100:
        print(f"There is a problem with the total weight")
    if formative_weight != 60:
        print("There is a problem with Formative weight")
    if summative_weight != 40:
        print("There is a problem with the summative weight")
    # TODO: c) Calculate the Final Grade and GPA
    final_grade = 0
    for item in data:
        grade = item['score'] * item['weight'] / 100
        final_grade += grade
    gpa = (final_grade / 100) * 5.0
    print(f"Your GPA is: {gpa}")
    # TODO: d) Determine Pass/Fail status (>= 50% in BOTH categories)
    cumulative_summative = 0
    cumulative_formative = 0
    for item in data:
        if item['group'] == "Formative":
            cumulative_formative += item['score'] * item['weight']
        if item['group'] == "Summative":
            cumulative_summative += item['score'] * item['weight']
    av_formative = cumulative_formative / formative_weight
    av_summative = cumulative_summative / summative_weight

    if av_formative >= 50 and av_summative >= 50:
        print("You have passed")
    else:
        print("You have failed")

    # TODO: e) Check for failed formative assignments (< 50%)
    #          and determine which one(s) have the highest weight for resubmission.
    failed = []
    highest_weight = 0
    for item in data:
        if item['group'] == 'Formative' and item['score'] < 50:
            failed.append(item)
    for ass in failed:
        if ass['weight'] > highest_weight:
            highest_weight = ass['weight']
    resubmit = False
    for ass in failed:
        if ass['weight'] == highest_weight:
            print(f"Eligible for resubmission: {ass['assignment']} assignment")
            resubmit = True
    if resubmit == False:
        print("No resubmissions needed.")
    
            

    # TODO: f) Print the final decision (PASSED / FAILED) and resubmission options
    
    pass

if __name__ == "__main__":
    # 1. Load the data
    course_data = load_csv_data()
    
    # 2. Process the features
    evaluate_grades(course_data)