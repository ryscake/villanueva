class Library:
    def __init__(self):
        self.books = []
        self.book_id_counter = 1

    def add_book(self, title, author):
        assert isinstance(title, str) and isinstance(author, str), 'Title and author must be strings'
        self.books.append({'id': self.book_id_counter, 'title': title, 'author': author, 'borrowed': False})
        print(f"Book added: {title} by {author} (ID: {self.book_id_counter})")
        self.book_id_counter += 1

    def borrow_book(self, title):
        for book in self.books:
            if book['title'].lower() == title.lower() and not book['borrowed']:
                book['borrowed'] = True
                print(f"You have borrowed '{title}'")
                return
            elif book['title'].lower() == title.lower() and book['borrowed']:
                print(f"'{title}' is already borrowed.")
                return
        print(f"'{title}' not found.")

    def return_book(self, title):
        for book in self.books:
            if book['title'].lower() == title.lower() and book['borrowed']:
                book['borrowed'] = False
                print(f"You have returned '{title}'")
                return
        print(f"'{title}' not found or not borrowed.")

    def display_books(self):
        available_books = [book for book in self.books if not book['borrowed']]
        if available_books:
            print("Available Books:")
            for book in available_books:
                print(f"ID: {book['id']}, Title: {book['title']}, Author: {book['author']}")
        else:
            print("No available books.")

    def check_book_id(self):
        try:
            book_id = int(input("Enter the book ID to check: "))
            for book in self.books:
                if book['id'] == book_id:
                    status = 'Borrowed' if book['borrowed'] else 'Available'
                    print(f"Book Found - Title: {book['title']}, Author: {book['author']}, Status: {status}")
                    return
            print(f"Book with ID {book_id} not found.")
        except ValueError as e:
            print(f"Invalid input: {e}")

    def lambda_example(self):
        title_lengths = list(map(lambda book: len(book['title']), self.books))
        for i, book in enumerate(self.books):
            print(f"{book['title']} - {title_lengths[i]} characters")

    def generate_numbers(self):
        for book in self.books:
            if book['borrowed']:
                pass
            else:
                yield book['id']

def menu():
    library = Library()
    global library_name
    library_name = "City Library"
    print(f"Welcome to {library_name}")
    while True:
        print("\nChoose an option:")
        print("1. Add Book")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Display Books")
        print("5. Check Book ID")
        print("6. Book title lengths")
        print("7. GenerateBook IDs")
        print("8. Exit")
        choice = input("Enter your choice (1-8): ")
        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            library.add_book(title, author)
        elif choice == '2':
            title = input("Enter book title to borrow: ")
            library.borrow_book(title)
        elif choice == '3':
            title = input("Enter book title to return: ")
            library.return_book(title)
        elif choice == '4':
            library.display_books()
        elif choice == '5':
            library.check_book_id()
        elif choice == '6':
            library.lambda_example()
        elif choice == '7':
            print("Generated book IDs of available books:", list(library.generate_numbers()))
        elif choice == '8':
            print("Exiting the library system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

menu()
