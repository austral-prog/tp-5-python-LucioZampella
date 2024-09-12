from src.Book import Book
from src.User import User


class Library:
    def __init__(self):
        self.__books = []
        self.__users = []
        self.__checked_out_books = {}  # ISBN: (DNI, due_date)
        self.__checked_in_books = set()  # ISBNs

    # Getters
    def get_books(self):
        return self.__books

    def get_users(self):
        return self.__users

    def get_checked_out_books(self):
        return self.__checked_out_books

    def get_checked_in_books(self):
        return self.__checked_in_books

    # 1.1 Add Book
    def add_book(self, isbn, title, author):
        new_book = Book(isbn, title, author)
        self.__books.append(new_book)
        self.__checked_in_books.add(isbn)

    # 1.2 List All Books
    def list_all_books(self):
        for book in self.__books:
            print(book)

    # 2.1 Check out book
    def check_out_book(self, isbn, dni, due_date):
        book = next((b for b in self.__books if b.get_isbn() == isbn), None)
        user = next((u for u in self.__users if u.get_dni() == dni), None)

        if not book or not user:
            return f"Unable to find the data for the values: ISBN {isbn} and DNI: {dni}"

        if not book.is_available():
            return f"Book {isbn} is not available"

        book.set_available(False)
        book.increment_checkout_num()
        user.increment_checkouts()
        self.__checked_out_books[isbn] = (dni, due_date)
        return f"User {dni} checked out book {isbn}"

    # 2.2 Check in book
    def check_in_book(self, isbn, dni, returned_date):
        if isbn not in self.__checked_in_books:
            return f"Book {isbn} is not available"
        if isbn not in self.__checked_out_books:
            return f"Book {isbn} is not available"
        book = next((b for b in self.__books if b.get_isbn() == isbn), None)
        if book:
            user_dni, _ = self.__checked_out_books[isbn]
            if user_dni != dni:
                return f"Book {isbn} was not checked out by user {dni}"
            book.set_available(True)
            self.__checked_out_books.pop(isbn)
            user = next((u for u in self.__users if u.get_dni() == dni), None)
            if user:
                user.increment_checkins()
                self.__checked_in_books.add(isbn)
                return f"Book {isbn} checked in by user {dni}"

        return f"Book {isbn} is not available"
    # Utils
    def add_user(self, dni, name):
        new_user = User(dni, name)
        self.__users.append(new_user)
