import json
import os

data_file = 'library.txt'
import json
import os

data_file = 'library.txt'

def load_library():
    if os.path.exists(data_file):
        with open(data_file, 'r') as file:
            return json.load(file)
    return []   

def save_library(library):
    with open(data_file, 'w') as file:
        json.dump(library, file)

        #yaha  hum se data option k sawal hon gay

def add_book(library):
    print("=========WELCOME TO PERSONAL LIBRARY===========")
    
    title = input('Enter the Title of the book: ')
    author = input('Enter the Author of the book: ')
    year = input('Enter the Year of the book: ')
    genre = input('Enter the Genre of the book: ')
    read = input('Have you read the book? (yes/no): ').lower() == 'yes'

    new_book = {
        'title': title,
        'author': author,
        'year': year,
        'genre': genre,
        'read' : read
    }

    library.append(new_book)
    save_library(library)
    print(f'Book {title} added successfully.')

def remove_book(library):
    title = input("Enter  the title book to remove from the library")   
    initial_length = len(library)
    library = [book for book in library if book['title'].lower() != title]
    if len(library) < initial_length:
        save_library(library)
        print(f'Book {title} removed successfully.')
    else:
        print(f'Book {title} not found in the library.')
 
def search_library(library):
    search_by = input("Search by title or author").lower()
    search_term = input(f"Enter the {search_by} ").lower()

    results = [book for book in library if search_term in book[search_by].lower()]

    if results:
        for book in results:
            status = "Read" if book['read'] else "Unread"
            print(f"{book['title']} by {book['author']} - {book['year']} - {book['genre']} - {status}")
    else:
        print(f"No books found matching '{search_term}' in the {search_by} field.")

def display_all_books(library):
    if library:
        for book in library:
            status = "Read" if book['read'] else "Unread"
            print(f"{book['title']} by {book['author']} - {book['year']} - {book['genre']} - {status}")
    else:
        print("The library is empty.")

def display_statistics(library):
    total_books = len(library)
    read_books = len([book for book in library if book['read']])
    percentage_read =  (read_books / total_books) * 100 if total_books > 0 else 0

    print(f"Total books: {total_books}")
    print(f"Percentage read : {percentage_read:.2f}%")


