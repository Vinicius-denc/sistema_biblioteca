import json

from pathlib import Path

FILE_JSON_PATH = Path(__file__).parent / 'library.json'

class Books():
    def __init__(self, name, writer, publisher, pages):
        self.name = name
        self.writer = writer
        self.publisher = publisher
        self.pages = pages


def load_bookcase(path, Books):

    bookcase = []# Criei a lista dentro da função para que não duplique os itens, a cada chamada uma nova lista
    with open(path, 'r', encoding='utf8') as file:
        book_files = json.load(file)

    for book in book_files:
        bookcase.append(Books(**book))

    return bookcase


def save_books(bookcase):

    formated_books = obj_to_dict(bookcase)

    with open(FILE_JSON_PATH, 'w', encoding='utf8') as file:
        json.dump(formated_books, file, indent=2)


def obj_to_dict(bookcase):
    formated_as_dict = []
    for book_obj in bookcase:
        formated_as_dict.append(vars(book_obj))
    return formated_as_dict


bookcase = []


book_3 = Books('Harry ', 'Rolling', 'Não sei', 200)
bookcase.append(book_3)
save_books(bookcase)

book_1 = Books('Harry Potter', 'J.K. Rolling', 'Não sei', 200)
bookcase.append(book_1)
save_books(bookcase)

book_2 = Books('Percy Jackson', 'Rick Riordan', 'Não sei', 150)
bookcase.append(book_2)
save_books(bookcase)



bookcase = load_bookcase(FILE_JSON_PATH, Books)


for book in bookcase:
    print(book.name)







