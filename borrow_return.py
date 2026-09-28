# Borrow and Return
def issue_book():
    B_id = input("Enter Book ID: ")
    S_id = input("Enter Student ID: ")
    stud_exists = False
    for stud in Students:
        if stud[0] == S_id:
            stud_exists = True
    if stud_exists == False:
        print("Student not found.")
        return
    for Book in Books:
        if Book[0] == B_id:
            if Book[3] == "Available":
                Book[3] = "Issued"
                print("Book issued successfully.")
            else:
                print("Book is already issued.")
            return
    print("Book not found.")
def return_book():
    B_id = input("Enter Book ID to return: ")
    for Book in Books:
        if Book[0] == B_id:
            if Book[3] == "Issued":
                Book[3] = "Available"
                print("Book returned successfully.")
            else:
                print("This book is already available.")
            return
    print("Book not found.")
def check_availability():
    B_id = input("Enter Book ID: ")
    for Book in Books:
        if Book[0] == B_id:
            if Book[3] == "Available":
                print("Book is available.")
            else:
                print("Book is currently issued.")
            return
    print("Book not found.")
