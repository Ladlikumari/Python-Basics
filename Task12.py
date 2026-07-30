"""Create a simple Student Management System using Python.

Requirements
Display a menu continuously until the user chooses Exit.

Menu options:
Add Student
View All Students
Search Student by Roll Number
Update Student Details
Delete Student
Exit

Each student should have:
Roll Number
Name
Age
Course

Store student data using a list of dictionaries. """



# Student Management System

students = []


# Add Student
def add_student():
    roll = input("Enter Roll Number: ")

    # Check duplicate roll number
    for student in students:
        if student["Roll"] == roll:
            print("Roll Number already exists!\n")
            return

    name = input("Enter Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")

    student = {
        "Roll": roll,
        "Name": name,
        "Age": age,
        "Course": course
    }

    students.append(student)
    print("Student Added Successfully!\n")


# View Students
def view_students():
    if not students:
        print("No Student Records Found!\n")
        return

    print("\n----- Student List -----")
    for student in students:
        print(f"Roll   : {student['Roll']}")
        print(f"Name   : {student['Name']}")
        print(f"Age    : {student['Age']}")
        print(f"Course : {student['Course']}")
        print("-" * 25)


# Search Student
def search_student():
    roll = input("Enter Roll Number to Search: ")

    for student in students:
        if student["Roll"] == roll:
            print("\nStudent Found")
            print(f"Roll   : {student['Roll']}")
            print(f"Name   : {student['Name']}")
            print(f"Age    : {student['Age']}")
            print(f"Course : {student['Course']}\n")
            return

    print("Student Not Found!\n")


# Update Student
def update_student():
    roll = input("Enter Roll Number to Update: ")

    for student in students:
        if student["Roll"] == roll:
            student["Name"] = input("Enter New Name: ")
            student["Age"] = input("Enter New Age: ")
            student["Course"] = input("Enter New Course: ")

            print("Student Updated Successfully!\n")
            return

    print("Student Not Found!\n")


# Delete Student
def delete_student():
    roll = input("Enter Roll Number to Delete: ")

    for student in students:
        if student["Roll"] == roll:
            students.remove(student)
            print("Student Deleted Successfully!\n")
            return

    print("Student Not Found!\n")


# Total Students
def total_students():
    print(f"\nTotal Students: {len(students)}\n")


# Main Program
while True:
    print("========== Student Management System ==========")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Total Students")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        total_students()

    elif choice == "7":
        print("Thank you for using Student Management System!")
        break

    else:
        print("Invalid Choice! Please try again.\n")

