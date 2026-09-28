# Book Management
def add_book():
    B_id = input("Enter the Book ID: ")
    Name = input("Enter the Book Name: ")
    Auth = input("Enter the Author's Name: ")
    Book = [B_id, Name, Auth, "Available"]
    Books.append(Book)
    print("Book has been added successfully.")
def remove_book():
    B_id = input("Enter the Book ID of the book to remove:")
    for Book in Books:
        if Book[0] == B_id:
            Books.remove(Book)
            print("Book has been removed successfully.")
            return
    print("Book not found.")
def search_book():
    B_id = input("Enter Book ID to search: ")
    for Book in Books:
        if Book[0] == B_id:
            print("Book ID:", Book[0])
            print("Book Name:", Book[1])
            print("Author:", Book[2])
            print("Status:", Book[3])
            return
    print("Book not found.")
