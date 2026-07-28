import os

# Always store students.txt in the same folder as this Python file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_NAME = os.path.join(BASE_DIR, "students.txt")


# ----------------------------
# File Handling Functions
# ----------------------------

def create_file():
    """Create students.txt if it does not exist."""
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w") as file:
            pass


def load_students():
    """Read students from students.txt."""

    create_file()

    students = []

    with open(FILE_NAME, "r") as file:
        for line in file:
            line = line.strip()

            if line:
                name, age, department = line.split(",")
                students.append([name, age, department])

    return students


def save_students(students):
    """Save all students into students.txt."""

    with open(FILE_NAME, "w") as file:
        for student in students:
            file.write(
                f"{student[0]},{student[1]},{student[2]}\n"
            )


# ----------------------------
# Add Student
# ----------------------------

def add_student():

    print("\n===== Add Student =====")

    name = input("Enter Name: ").strip()
    age = input("Enter Age: ").strip()
    department = input("Enter Department: ").strip()


    if not name or not department:
        print("❌ Fields cannot be empty")
        return


    if not age.isdigit():
        print("❌ Age must be a number")
        return


    students = load_students()


    # Duplicate checking
    for student in students:
        if student[0].lower() == name.lower():
            print("❌ Student already exists")
            return


    students.append([name, age, department])

    save_students(students)

    print("✅ Student added successfully")


# ----------------------------
# View Students
# ----------------------------

def view_students():

    print("\n===== Student Records =====")

    students = load_students()


    if not students:
        print("No records found")
        return


    for i, student in enumerate(students, 1):

        print("\nStudent", i)
        print("Name:", student[0])
        print("Age:", student[1])
        print("Department:", student[2])


# ----------------------------
# Search Student
# ----------------------------

def search_student():

    name = input("Enter student name: ").strip()

    students = load_students()


    for student in students:

        if student[0].lower() == name.lower():

            print("\nStudent Found")
            print("----------------")
            print("Name:", student[0])
            print("Age:", student[1])
            print("Department:", student[2])
            return


    print("❌ Student not found")


# ----------------------------
# Update Student
# ----------------------------

def update_student():

    name = input("Enter student name to update: ").strip()

    students = load_students()


    for student in students:

        if student[0].lower() == name.lower():

            new_age = input("Enter new age: ")
            new_department = input("Enter new department: ")


            student[1] = new_age
            student[2] = new_department


            save_students(students)


            print("✅ Student updated successfully")
            return


    print("❌ Student not found")


# ----------------------------
# Delete Student
# ----------------------------

def delete_student():

    name = input("Enter student name to delete: ").strip()


    students = load_students()


    updated_students = []


    deleted = False


    for student in students:

        if student[0].lower() == name.lower():

            deleted = True

        else:
            updated_students.append(student)


    if deleted:

        save_students(updated_students)

        print("✅ Student deleted successfully")

    else:

        print("❌ Student not found")


# ----------------------------
# Total Students
# ----------------------------

def total_students():

    students = load_students()

    print(
        "Total Students:",
        len(students)
    )


# ----------------------------
# Main Menu
# ----------------------------

def menu():

    while True:

        print("""
=================================
 Student Record Management System
=================================

1. Add Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student
6. Total Students
7. Exit
""")


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
            print("Thank you!")
            break

        else:
            print("Invalid choice")


# Start program

if __name__ == "__main__":
    menu()