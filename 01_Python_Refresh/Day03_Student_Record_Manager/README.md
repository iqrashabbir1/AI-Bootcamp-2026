# Day 03 – Student Record Management System

## 📌 Project Overview

The **Student Record Management System** is a Python-based command-line application that manages student information using file handling.

The application allows users to add, view, search, update, and delete student records. All records are stored permanently in a text file (`students.txt`).

This project demonstrates basic **CRUD operations** (Create, Read, Update, Delete) using Python.

---

## 🎯 Learning Objectives

By completing this project, I learned:

* File handling in Python
* Reading and writing data to files
* Creating reusable functions
* Implementing CRUD operations
* Using lists and loops
* Input validation
* Exception handling concepts
* Building menu-driven applications
* Managing projects using Git and GitHub

---

## 🛠 Technologies Used

* Python 3
* Visual Studio Code
* Git
* GitHub

---

## ✨ Features

### 1. Add Student

* Add new student records
* Store data permanently in `students.txt`
* Prevent duplicate student entries

### 2. View Students

* Display all saved student records

### 3. Search Student

* Search students by name

### 4. Update Student

* Modify existing student information
* Save updated data automatically

### 5. Delete Student

* Remove student records permanently

### 6. Student Statistics

* Display total number of students

---

## 📂 Project Structure

```text
Day03_Student_Record_Manager
│
├── student_manager.py
├── students.txt
├── README.md
├── sample_output.txt
└── screenshots
    └── student_manager_output.png
```

---

## 🚀 How to Run

1. Open the project folder in VS Code.

2. Open the terminal.

3. Run:

```bash
python student_manager.py
```

4. Select options from the menu.

---

## 💻 Example Output

```text
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


Enter your choice: 1

Enter Name: Iqra
Enter Age: 35
Enter Department: AI Robotics

Student added successfully
```

---

## 📸 Output Screenshot

Add your screenshot here:

```markdown
![Student Manager Output](screenshots/student_manager_output.png)
```

---

## 📄 Data Storage Example

The student records are stored in:

```text
students.txt
```

Example:

```text
Iqra,35,AI Robotics
Ali,22,Computer Science
Sara,24,Data Science
```

---

## 🔄 Future Improvements

Possible improvements:

* Add student ID generation
* Export records to CSV
* Create a graphical user interface (GUI)
* Connect with a database such as SQLite
* Add user authentication
* Build a web version using Flask/Django

---

## 👩‍💻 Author

**Iqra Shabbir**

AI Bootcamp 2026

Day 03 – Student Record Management System
