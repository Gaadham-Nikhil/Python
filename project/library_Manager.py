import json

def store():
    try:
        with open('project/Books.txt', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def issued_books_store():
    try:
        with open('project/Issued_books.txt', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_to_file(books):
    with open('project/Books.txt', 'w') as file:
        json.dump(books, file)

def save_to_issued_file(issued_books):
    with open('project/Issued_books.txt', 'w') as file:
        json.dump(issued_books, file)

def list_of_books(books):
    print('- - ' * 12)
    for index, book in enumerate(books, start=1):
        print(f"{index}.Book-Id: {book['book_id']}\n  Name: {book['name']}")
    print('---' * 12)

def list_of_issued_books(issued_books):
    print("- - "*12)
    for index, book in enumerate(issued_books, start=1):
        print(f"{index}.Book Name:{book['name']}\n  Assigned-to:{book['assigned_to']}")
    print("- - "*12)


def add_book(books):
    book_id = int(input("Enter Book Id: "))
    name = input("Enter book Name: ")
    books.append({'book_id': book_id, 'name': name,})
    save_to_file(books)
    print("Added Successfully!!!")

def issue_book(issued_books):
    book_id = int(input("Enter Book Id: "))
    name = input("Enter book Name: ")
    assigned_to = input("Name of the Student Assigned to: ")
    issued_books.append({'book_id': book_id, 'name': name, 'assigned_to': assigned_to})
    save_to_issued_file(issued_books)


def remove_book(books):
    list_of_books(books)
    idx = int(input("Enter Book index number: "))
    if 1 <= idx <= len(books):
        del books[idx-1]
        save_to_file(books)
    else:
        print("Invalid selection of Index value\n")

def main():
    books = store()
    issued_books = issued_books_store()
    while True:
        print("Library Management System | Choose an Option")
        print("1. List of all Books")
        print("2. List of issued Books")
        print("3. Add a Book")
        print("4. Issue a Book")
        print("5. Remove a Book")
        print("6. Exit the App")

        choice = input("Enter your choice: ")
        
        match choice:
            case '1':
                list_of_books(books)
            case '2':
                list_of_issued_books(issued_books)
            case '3':
                add_book(books)
            case '4':
                issue_book(issued_books)
            case '5':
                remove_book(books)
            case '6':
                break
            case _:
                print("Invalid Option Selected. Please Select Correct Option!!!")

if __name__ == "__main__":
    main()