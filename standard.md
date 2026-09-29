📚 Library Management System
1. 📝 Problem Statement

Managing books and student records manually can be time-consuming and may lead to difficulties when searching for information or checking book availability. It can also be difficult to keep track of which books have been issued or returned.

The purpose of this project is to develop a simple Python-based Library Management System that helps manage book records, student records, and basic borrowing and returning operations through a menu-driven interface.

2. 🎯 Scope of the Project

The project focuses on the basic management of books and students in a library. It allows the user to add, remove, and search for books and students. It also provides functionality for issuing books, returning books, and checking book availability.

The current version stores the information temporarily using Python lists while the program is running. It does not include a database or permanent storage.

The project is intended as a basic Python programming application and can be extended in the future with features such as database storage, login systems, due dates, and fine calculation.

3. 👥 Target Users

The main target users of the system are:

👨‍💼 Librarians: To manage books, students, and borrowing activities.
🧑‍💼 Library Staff: To add, remove, and search records and check book availability.
🎓 Students: Student records can be maintained in the system, while library staff can use the system to issue and return books.

The current version is designed mainly for demonstration and educational purposes rather than deployment in a large library.

4. ⭐ High-Level Features
📖 Book Management
➕ Add a new book
❌ Remove a book
🔍 Search for a book
📗 Check book availability
🎓 Student Management
➕ Add a student
❌ Remove a student
🔍 Search for a student
📋 Display all students
🔄 Borrow and Return
📤 Issue a book to a registered student
📥 Return an issued book
✅ Check whether a book is available or issued
🖥️ User Interface
📋 Menu-driven interface
🔹 Separate menus for different operations
💬 Messages for successful operations and invalid inputs
💾 Data Handling
📚 Book records stored using Python lists
👥 Student records stored using Python lists
🔄 Book status updated between "Available" and "Issued"
