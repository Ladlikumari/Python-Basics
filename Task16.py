"""Create a file student.txt and store the names and marks of 5 students. Then:

Read and display the data
Find the student with the highest marks
Count the total number of students"""


# Create and write data into the file
with open("student.txt", "w") as file:
    file.write("Rahul,85\n")
    file.write("Priya,92\n")
    file.write("Aman,78\n")
    file.write("Neha,95\n")
    file.write("Riya,88\n")


# Read data from the file
with open("student.txt", "r") as file:
    data = file.readlines()


students = []

for line in data:
    name, marks = line.strip().split(",")
    students.append((name, int(marks)))


# Display student details
print("Student Details:")

for name, marks in students:
    print(name, "-", marks)


# Find highest scorer
highest = max(students, key=lambda x: x[1])

print("\nHighest Scorer:", highest[0], "-", highest[1])


# Count total students
print("Total Students:", len(students))