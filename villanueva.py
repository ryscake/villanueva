class Library:
    def __init__(self):
        self.books = []
        self.book_id_counter = 1

    def add_book(self, title, author):
        assert isinstance(title, str) and isinstance(author, str), 'title and author must be strings'
        self.books.append({'id': self.book_id_counter, 'title': title, 'author': author, 'borrowed': False})
        print(f"book added: {title} by {author} (ID: {self.book_id_counter})")
        self.book_id_counter += 1

    def borrow_book(self, title):
        for book in self.books:
            if book['title'].lower() == title.lower() and not book['borrowed']:
                book['borrowed'] = True
                print(f"you have borrowed '{title}'")
                return
            elif book['title'].lower() == title.lower() and book['borrowed']:
                print(f"'{title}' is already borrowed.")
                return
        print(f"'{title}' not found.")

    def return_book(self, title):
        for book in self.books:
            if book['title'].lower() == title.lower() and book['borrowed']:
                book['borrowed'] = False
                print(f"you have returned '{title}'")
                return
        print(f"'{title}' not found or not borrowed.")

    def display_books(self):
        available_books = [book for book in self.books if not book['borrowed']]
        if available_books:
            print("available Books:")
            for book in available_books:
                print(f"ID: {book['id']}, title: {book['title']}, author: {book['author']}")
        else:
            print("no available books.")

    def check_book_id(self):
        try:
            book_id = int(input("enter the book ID to check: "))
            for book in self.books:
                if book['id'] == book_id:
                    status = 'borrowed' if book['borrowed'] else 'available'
                    print(f"book Found - title: {book['title']}, author: {book['author']}, status: {status}")
                    return
            print(f"book with ID {book_id} not found.")
        except ValueError as e:
            print(f"invalid input: {e}")

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
    library_name = "Library Ng Lahat"
    print(f"Welcome to {library_name}")
    while True:
        print("\nChoose an option:")
        print("1. add Book")
        print("2. borrow Book")
        print("3. return Book")
        print("4. display Books")
        print("5. check Book ID")
        print("6. book title lengths")
        print("7. generateBook IDs")
        print("8. exit")
        choice = input("enter your choice (1-8): ")
        if choice == '1':
            title = input("enter book title: ")
            author = input("enter book author: ")
            library.add_book(title, author)
        elif choice == '2':
            title = input("enter book title to borrow: ")
            library.borrow_book(title)
        elif choice == '3':
            title = input("enter book title to return: ")
            library.return_book(title)
        elif choice == '4':
            library.display_books()
        elif choice == '5':
            library.check_book_id()
        elif choice == '6':
            library.lambda_example()
        elif choice == '7':
            print("generated book IDs of available books:", list(library.generate_numbers()))
        elif choice == '8':
            print("exiting the library system. goodbye!")
            break
        else:
            print("invalid choice. Please try again.")

menu()
