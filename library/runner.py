import random
import threading
import time
import datetime
from library.Library import Library

__author__ = 'ekamoliddinov'

library = Library()


def get_random_book():
    global library
    rnd = random.randint(1, len(library.books.keys()) - 1)
    return list(library.books.keys())[rnd]


def get_random_user():
    global library
    rnd = random.randint(1, len(library.users) - 1)
    return library.users[rnd]


def giver():
    global library
    while True:
        book = get_random_book()
        user = get_random_user()
        library.give(user, book)
        time.sleep(random.randint(20, 40))


def returner():
    global library
    while True:
        user = get_random_user()
        bk = user.get_random_book()
        if bk is not None:
            library.return_b(user, user.get_random_book())
        time.sleep(random.randint(20, 40))


def stat():
    while True:
        arg = raw_input("Insert stat to see the current book history status... \n")
        if arg == 'stat':
            with open("stat.txt", "a") as f:
                f.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S").center(100, '-') + "\n")
                for u in library.users:
                    f.write(str(10 * " " + "User " + u.name + " book history").ljust(50))
                    f.write("\n")
                    f.write("\n")
                    for bh in u.bookHistory:
                        f.write('{0:35} ==> {1:50}'.format(15 * " " + bh.book.title,
                                                           bh.date.strftime("%Y-%m-%d %H:%M:%S")))
                        f.write("\n")
                    if len(u.bookHistory) > 0:
                        f.write("\n")


for t in range(1, 3):
    threading.Thread(target=giver, name='Giver-' + str(t)).start()

for t in range(1, 3):
    threading.Thread(target=returner, name='Returner-' + str(t)).start()

daemon_thread = threading.Thread(target=stat, name='Daemon')
daemon_thread.setDaemon(True)
daemon_thread.start()