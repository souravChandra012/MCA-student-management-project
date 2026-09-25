import json

FILE_NAME = "students.json"


# -----------------------------
# Student Class
# -----------------------------
class Student:
    def __init__(self, student_id, name, semester, python_marks,
                 dbms_marks, dsa_marks, os_marks):

        self.student_id = student_id
        self.name = name
        self.semester = semester
        self.python_marks = python_marks
        self.dbms_marks = dbms_marks
        self.dsa_marks = dsa_marks
        self.os_marks = os_marks

    # Calculate total marks
    def calculate_total(self):
        return (
            self.python_marks +
            self.dbms_marks +
            self.dsa_marks +
            self.os_marks
        )

    # Calculate percentage
    def calculate_percentage(self):
        return self.calculate_total() / 4

    # Calculate grade
    def calculate_grade(self):
        percentage = self.calculate_percentage()

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

    # Convert object into dictionary
    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "semester": self.semester,
            "python_marks": self.python_marks,
            "dbms_marks": self.dbms_marks,
            "dsa_marks": self.dsa_marks,
            "os_marks": self.os_marks
        }


# -----------------------------
# Load Students
# -----------------------------
def load_students():

    try:
        with open(FILE_NAME, "r") as file:
            data = json.load(file)

        students = {}

        for student_id, details in data.items():

            students[student_id] = Student(
                details["student_id"],
                details["name"],
                details["semester"],
                details["python_marks"],
                details["dbms_marks"],
                details["dsa_marks"],
                details["os_marks"]
            )

        return students

    except FileNotFoundError:
        return {}


# -----------------------------
# Save Students
# -----------------------------
def save_students(students):

    data = {}

    for student_id, student in students.items():
        data[student_id] = student.to_dict()

    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

    print("\nData saved successfully!")


# -----------------------------
# Add Student
# -----------------------------
def add_student(students):

    print("\n========== ADD STUDENT ==========")

    student_id = input("Enter Student ID: ")

    if student_id in students:
        print("Student ID already exists!")
        return

    name = input("Enter Student Name: ")
    semester = input("Enter Semester: ")

    python_marks = float(input("Enter Python Marks: "))
    dbms_marks = float(input("Enter DBMS Marks: "))
    dsa_marks = float(input("Enter DSA Marks: "))
    os_marks = float(input("Enter OS Marks: "))

    student = Student(
        student_id,
        name,
        semester,
        python_marks,
        dbms_marks,
        dsa_marks,
        os_marks
    )

    students[student_id] = student

    save_students(students)

    print("Student added successfully!")


# -----------------------------
# View Students
# -----------------------------
def view_students(students):

    print("\n========== ALL STUDENTS ==========")

    if not students:
        print("No students found.")
        return

    for student in students.values():

        print("\n------------------------------")

        print("Student ID :", student.student_id)
        print("Name       :", student.name)
        print("Semester   :", student.semester)

        print("Python     :", student.python_marks)
        print("DBMS       :", student.dbms_marks)
        print("DSA        :", student.dsa_marks)
        print("OS         :", student.os_marks)

        print("Total      :", student.calculate_total())
        print("Percentage :", student.calculate_percentage())
        print("Grade      :", student.calculate_grade())


# -----------------------------
# Search Student
# -----------------------------
def search_student(students):

    print("\n========== SEARCH STUDENT ==========")

    student_id = input("Enter Student ID: ")

    if student_id not in students:
        print("Student not found!")
        return

    student = students[student_id]

    print("\nStudent Found!")

    print("------------------------------")
    print("Student ID :", student.student_id)
    print("Name       :", student.name)
    print("Semester   :", student.semester)

    print("Python     :", student.python_marks)
    print("DBMS       :", student.dbms_marks)
    print("DSA        :", student.dsa_marks)
    print("OS         :", student.os_marks)

    print("Total      :", student.calculate_total())
    print("Percentage :", student.calculate_percentage())
    print("Grade      :", student.calculate_grade())


# -----------------------------
# Update Student
# -----------------------------
def update_student(students):

    print("\n========== UPDATE STUDENT ==========")

    student_id = input("Enter Student ID: ")

    if student_id not in students:
        print("Student not found!")
        return

    student = students[student_id]

    print("\nEnter new information:")

    student.name = input("Enter Name: ")
    student.semester = input("Enter Semester: ")

    student.python_marks = float(
        input("Enter Python Marks: ")
    )

    student.dbms_marks = float(
        input("Enter DBMS Marks: ")
    )

    student.dsa_marks = float(
        input("Enter DSA Marks: ")
    )

    student.os_marks = float(
        input("Enter OS Marks: ")
    )

    save_students(students)

    print("Student updated successfully!")


# -----------------------------
# Delete Student
# -----------------------------
def delete_student(students):

    print("\n========== DELETE STUDENT ==========")

    student_id = input("Enter Student ID: ")

    if student_id not in students:
        print("Student not found!")
        return

    confirm = input(
        "Are you sure you want to delete this student? (y/n): "
    )

    if confirm.lower() == "y":

        del students[student_id]

        save_students(students)

        print("Student deleted successfully!")

    else:
        print("Delete operation cancelled.")


# -----------------------------
# Main Menu
# -----------------------------
def main():

    students = load_students()

    while True:

        print("\n")
        print("==========================================")
        print("       MCA STUDENT MANAGEMENT SYSTEM")
        print("==========================================")

        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Save Data")
        print("7. Exit")

        print("==========================================")

        choice = input("Enter your choice: ")

        if choice == "1":

            add_student(students)

        elif choice == "2":

            view_students(students)

        elif choice == "3":

            search_student(students)

        elif choice == "4":

            update_student(students)

        elif choice == "5":

            delete_student(students)

        elif choice == "6":

            save_students(students)

        elif choice == "7":

            save_students(students)

            print("\nThank you for using MCA Student Management System!")
            break

        else:

            print("Invalid choice! Please try again.")


# -----------------------------
# Program Start
# -----------------------------
if __name__ == "__main__":
    main()