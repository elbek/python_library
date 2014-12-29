import logging
import random
import threading
from library.Book import Book
from library.User import User

__author__ = 'ekamoliddinov'

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s (%(threadName)-2s) %(message)s', )


class Library:
    def __init__(self):
        self.books = dict([])
        self.users = []
        self.__load_books()
        self.__load_users()

    def __load_books(self):
        with open("books.txt") as f:
            for line in f:
                lock = threading.Lock()
                bk = Book(line.rstrip())
                self.books[bk] = lock

    def __load_users(self):
        with open("users.txt") as f:
            for line in f:
                us = User(line.rstrip())
                self.users.append(us)

    def stats(self):
        for u in self.users:
            pass

    def give(self, user, book):
        with self.books[book]:
            if book.copies == book.taken:
                logging.warning("This book %s is not available for user %s", book.title, user.name)
                return
            if book in user.books:
                logging.error("This book %s is already rented by user %s, no double rents allowed", book.title, user.name)
                return
            if len(user.books) > 2:
                logging.error("This user %s, rented already 3 books", user.name)
                return
            book.taken += 1
            user.add_book(book)

    def return_b(self, user, book):
        with self.books[book]:
            if not book in user.books:
                logging.error("This book %s is not rented by user %s", book.title, user.name)
                return
            book.taken -= 1
            user.return_book(book)