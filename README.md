# 📚 Library Management System

## 📌 1. Project Overview

The **Library Management System** is a simple Python-based application designed to manage basic library activities. The system allows users to manage book and student records and handle basic book borrowing and returning operations.

The project uses a menu-driven interface, making it simple for the user to select and perform different operations.

Book and student information is stored temporarily using Python lists while the program is running.

---

## ✨ 2. Features

### 📖 Book Management

* ➕ Add a new book
* ❌ Remove a book
* 🔍 Search for a book
* 📗 Check book availability

### 🎓 Student Management

* ➕ Add a student
* ❌ Remove a student
* 🔍 Search for a student
* 📋 Display all students

### 🔄 Borrow / Return

* 📤 Issue a book to a student
* 📥 Return an issued book
* ✅ Check book availability
* 🔄 Automatically update book status between `"Available"` and `"Issued"`

### 🖥️ Menu System

* 📋 Main menu for accessing different sections
* 🔹 Separate menus for Book Management, Student Management, and Borrow/Return
* 💬 Messages for successful operations and invalid inputs

---

## 🛠️ 3. Technologies / Tools Used

* 🐍 **Python**
* 📝 **Python Lists**
* 🔧 **Python Functions**
* 🔁 **Loops**
* 🔀 **Conditional Statements**
* ⌨️ **User Input**
* 💻 **Google Colab / Python**
* 🐙 **GitHub** for project storage and version control

---

## ⚙️ 4. Installation & Running

### Step 1: Download the Project

Clone the repository using Git:

```text
git clone <repository-link>
```

Or download the project files directly from GitHub.

### Step 2: Open the Project Folder

Make sure the following files are present in the same folder:

```text
Library-Management-System/
│
├── main.py
├── book_management.py
├── student_management.py
├── borrow_return.py
├── README.md
└── standard.md
```

### Step 3: Install Python

Make sure Python is installed on your computer.

Python 3 or a later compatible version is recommended.

### Step 4: Run the Program

Open a terminal or command prompt inside the project folder and run:

```text
python main.py
```

The Library Management System will start and display the main menu.

```text
===== LIBRARY MANAGEMENT SYSTEM =====

1. Book Management
2. Student Management
3. Borrow / Return
4. Exit
```

Select an option and follow the instructions displayed by the program.

---

## 🧪 5. Testing Instructions

The project can be tested by running `main.py` and checking each feature individually.

### 📖 Test Book Management

1. Select **Book Management**.
2. Add a book using a Book ID, name, and author's name.
3. Search for the book using its Book ID.
4. Check that the correct book information is displayed.
5. Remove the book and verify that it is no longer found.

### 🎓 Test Student Management

1. Select **Student Management**.
2. Add a student using a Student ID, name, and course.
3. Search for the student using the Student ID.
4. Use **Display Students** to check the stored student records.
5. Remove the student and verify that the record has been removed.

### 🔄 Test Borrow / Return

1. Add a student and a book first.
2. Select **Borrow / Return**.
3. Choose **Issue Book** and enter the Book ID and Student ID.
4. Check that the message **"Book issued successfully."** is displayed.
5. Use **Check Availability** to confirm that the book is now issued.
6. Select **Return Book**.
7. Check the availability again and confirm that the book is available.

### ⚠️ Test Invalid Inputs

The following situations should also be tested:

* Entering a Book ID that does not exist.
* Entering a Student ID that does not exist.
* Trying to issue an already issued book.
* Trying to return an available book.
* Entering an invalid menu option.

The system should display an appropriate message for each situation.

---

## 📁 Project Structure

```text
Library-Management-System/
│
├── main.py
├── book_management.py
├── student_management.py
├── borrow_return.py
├── README.md
└── standard.md
```

## 👨‍💻 Author

**Hemanga Kalita**
**26BCE10990**
**VIT Bhopal University**
