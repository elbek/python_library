import datetime
import logging
import random
import threading

__author__ = 'ekamoliddinov'

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s (%(threadName)-2s) %(message)s', )


class User:
    def __init__(self, name):
        self.books = set([])
        self.bookHistory = []
        self.name = name
        self.lock = threading.Lock()

    def add_book(self, book):
        with self.lock:
            self.books.add(book)
            self.bookHistory.append(BookHistory(book))
            logging.debug("This book %s is rented by user %s", book.title, self.name)

    def get_random_book(self):
        with self.lock:
            if len(self.books) == 0:
                return None
            return list(self.books)[random.randint(0, len(self.books)-1)]

    def return_book(self, book):
        with self.lock:
            self.books.remove(book)
            logging.debug("This book %s is returned by user %s", book.title, self.name)

    def __repr__(self):
        return "name: " + self.name


class BookHistory:
    def __init__(self, book):
        self.book = book
        self.date = datetime.datetime.now()