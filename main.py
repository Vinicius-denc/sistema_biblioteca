import json
from pathlib import Path

FILE_JSON_PATH = Path(__file__).parent / 'library.json'
class Books():
    def __init__(self, name, writer, publisher, pages):
        self.name = name
        self.writer = writer
        self.publisher = publisher
        self.pages = pages



book_1 = Books('Harry Potter', 'J.K. Rolling', 'Não sei', 200)
book_2 = Books('Percy Jackson', 'Rick Riordan', 'Não sei', 150)

backup_list_for_json = [vars(book_1), vars(book_2)]

# with open(FILE_JSON_PATH, 'w', encoding='utf8') as file:
#     json.dump(backup_list_for_json, file, indent=2)



with open(FILE_JSON_PATH, 'r', encoding='utf8') as file:
    books_files = json.load(file)

bookcase = []
for book in books_files:
    bookcase.append(Books(**book))

for book in bookcase:
    print(book.name)






