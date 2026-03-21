# Lab 1 - Grade Evaluator & Archiver

A Python application that evaluates student grades from a CSV file and determines academic standing, paired with a Bash script for automated file archiving and logging.

## Files

- `grade-evaluator.py` — Python script that validates grades, calculates GPA, determines pass/fail status, and identifies resubmission eligibility.
- `organizer.sh` — Bash script that archives the grades CSV file with a timestamp and logs the operation.
- `grades.csv` — CSV file containing student assignment data (assignment name, group, score, weight).

## How to Run

### Grade Evaluator (Python)

Make sure `grades.csv` is in the same directory, then run:

```bash
python3 grade-evaluator.py
```

The program will prompt you to enter the CSV filename. Type `grades.csv` and press Enter. It will display a full report including score validation, weight validation, final grade, GPA, pass/fail status, and resubmission eligibility.

### Organizer (Bash)

Run the script from the project directory:

```bash
bash organizer.sh
```

This will:
1. Create an `archive` directory if it does not exist.
2. Rename `grades.csv` with a timestamp and move it into `archive/`.
3. Create a new empty `grades.csv` in the current directory.
4. Log the operation in `organizer.log`.

## Requirements

- Python 3
- Bash shell (Linux, macOS, or Git Bash on Windows)
