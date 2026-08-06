
"""Python Task 13 – Advanced Practice

Question: Write a Python program for a Student Result Management System.

Your program should:

Take student name and roll number.
Take marks for 5 subjects.
Calculate total marks, percentage, and grade.
Display Pass/Fail status.
Find the highest and lowest marks.
Use functions, dictionary, loops, and if-elif-else.

Grade criteria:

90% and above → A+
80–89% → A
70–79% → B
60–69% → C
50–59% → D
Below 50% → F

Extra condition: If the student gets less than 35 marks in any subject, the final result should be Fail, regardless of overall percentage.

Example output:

===== STUDENT RESULT =====
Name       : Ladli
Roll No    : 101
Total      : 408/500
Percentage : 81.60%
Grade      : A
Highest    : 92
Lowest     : 72
Result     : PASS"""



# Task 13: Student Result Management System

def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"


def student_result():
    student = {}

    # Student details
    student["name"] = input("Enter student name: ")
    student["roll_no"] = input("Enter roll number: ")

    subjects = ["Math", "English", "Science", "Computer", "Physics"]
    marks = {}

    # Taking marks
    for subject in subjects:
        marks[subject] = float(input(f"Enter marks for {subject}: "))

    student["marks"] = marks

    # Calculations
    total = sum(marks.values())
    percentage = total / len(subjects)

    highest = max(marks.values())
    lowest = min(marks.values())

    grade = calculate_grade(percentage)

    # Pass/Fail condition
    if lowest < 35:
        result = "FAIL"
    else:
        result = "PASS"

    # Display result
    print("\n===== STUDENT RESULT =====")
    print("Name       :", student["name"])
    print("Roll No    :", student["roll_no"])
    print("Total      :", total, "/ 500")
    print(f"Percentage : {percentage:.2f}%")
    print("Grade      :", grade)
    print("Highest    :", highest)
    print("Lowest     :", lowest)
    print("Result     :", result)


# Function call
student_result()