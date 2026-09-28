# Student Management
def add_student():
    S_id = input("Enter Student ID: ")
    Name = input("Enter Student Name: ")
    Course = input("Enter Course: ")
    Stud = [S_id, Name, Course]
    Students.append(Stud)
    print("Student added successfully.")
def remove_student():
    S_id = input("Enter Student ID to remove: ")
    for Stud in Students:
        if Stud[0] == S_id:
            Students.remove(Stud)
            print("Student removed successfully.")
            return
    print("Student not found.")
def search_student():
    S_id = input("Enter Student ID to search: ")
    for Stud in Students:
        if Stud[0] == S_id:
            print("Student ID:", Stud[0])
            print("Student Name:", Stud[1])
            print("Course:", Stud[2])
            return
    print("Student not found.")
def display_students():
    if len(Students) == 0:
        print("No students found.")
    else:
        print("\nStudents in the Library System:")
        for Stud in Students:
            print("ID:", Stud[0])
            print("Name:", Stud[1])
            print("Course:", Stud[2])
            print("--------------------")
