import csv
import os

FILE_NAME = "students.csv"

def create_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Name", "Age", "Gender", "Marks"])

def add_student():
    student_id = input("Enter Student ID: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    gender = input("Enter Gender: ")
    marks = input("Enter Marks: ")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([student_id, name, age, gender, marks])

    print("Student added successfully.")

def display_students():
    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)
        students = list(reader)

    if not students:
        print("No student records found.")
        return

    print("\nStudent Records")
    print("-" * 75)

    for student in students:
        print(
            f"ID: {student['ID']} | "
            f"Name: {student['Name']} | "
            f"Age: {student['Age']} | "
            f"Gender: {student['Gender']} | "
            f"Marks: {student['Marks']}"
        )

def search_student():
    student_id = input("Enter Student ID to search: ")

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)

        for student in reader:
            if student["ID"] == student_id:
                print("\nStudent Found")
                print("ID:", student["ID"])
                print("Name:", student["Name"])
                print("Age:", student["Age"])
                print("Gender:", student["Gender"])
                print("Marks:", student["Marks"])
                return

    print("Student not found.")

def update_student():
    student_id = input("Enter Student ID to update: ")

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)
        students = list(reader)

    found = False

    for student in students:
        if student["ID"] == student_id:
            student["Name"] = input("Enter new Name: ")
            student["Age"] = input("Enter new Age: ")
            student["Gender"] = input("Enter new Gender: ")
            student["Marks"] = input("Enter new Marks: ")
            found = True
            break

    if found:
        with open(FILE_NAME, "w", newline="") as file:
            fieldnames = ["ID", "Name", "Age", "Gender", "Marks"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(students)

        print("Student record updated successfully.")
    else:
        print("Student not found.")

def delete_student():
    student_id = input("Enter Student ID to delete: ")

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)
        students = list(reader)

    new_students = [student for student in students if student["ID"] != student_id]

    if len(new_students) == len(students):
        print("Student not found.")
        return

    with open(FILE_NAME, "w", newline="") as file:
        fieldnames = ["ID", "Name", "Age", "Gender", "Marks"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(new_students)

    print("Student record deleted successfully.")

def sort_students():
    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)
        students = list(reader)

    students.sort(key=lambda x: float(x["Marks"]), reverse=True)

    print("\nStudents Sorted by Marks")
    print("-" * 75)

    for student in students:
        print(
            f"ID: {student['ID']} | "
            f"Name: {student['Name']} | "
            f"Age: {student['Age']} | "
            f"Gender: {student['Gender']} | "
            f"Marks: {student['Marks']}"
        )

create_file()

while True:
    print("\n===== STUDENT RECORD HANDLING =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Sort Students by Marks")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        sort_students()
    elif choice == "7":
        print("Program ended.")
        break
    else:
        print("Invalid choice.")