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

    return bookcase #lista de objetos



def save_books(bookcase):

    formated_books = obj_to_dict(bookcase)

    with open(FILE_JSON_PATH, 'w', encoding='utf8') as file:
        json.dump(formated_books, file, indent=2)



def obj_to_dict(bookcase):
    formated_as_dict = []
    for book_obj in bookcase:
        formated_as_dict.append(vars(book_obj))
    return formated_as_dict #lista de dicionarios


def add_book():
    create_a_book = {
        'name': None,
        'writer': None,
        'publisher': None,
        'pages': None
    }
    
    while not create_a_book['name']:
        create_a_book['name'] = input('Nome do livro:').strip()
        if not create_a_book['name']:
            print('O nome do livro não pode ficar vazio')

    while not create_a_book['writer']:
        create_a_book['writer'] = input('Autor(a):').strip()
        if not create_a_book['writer']:
            print('O nome do autor(a) não pode ficar vazio')

    while not create_a_book['publisher']:
        create_a_book['publisher'] = input('Editora:').strip()
        if not create_a_book['publisher']:
            print('O nome da editora não pode ficar vazio')
    
    while True:
        try:
            create_a_book['pages'] = int(input('Número de páginas:'))
            if create_a_book['pages'] <= 0:
                print('Digite um número de páginas válido')
                continue
            break
        except ValueError:
            print('Digite um número de páginas válido')
        
    
    book_created = Books(**create_a_book)
    return book_created #retorna um objeto de livro


def show_saved_books(bookcase):
    books = obj_to_dict(bookcase)
    for index, book in enumerate(books, start= 1):
        print(f"{index} - {book['name']}")
        print(f"Autor: {book['writer']}")
        print(f"Editora: {book['publisher']}")
        print(f"Páginas: {book['pages']}")
        print()
    

def del_book(bookcase):
    if bookcase:
        try:
            book_to_delete = int(input('Digite o indice do livro a ser deletado: '))
            if book_to_delete <= 0 or book_to_delete > len(bookcase):
                print('Indice não encontrado')
            else:
                bookcase.pop(book_to_delete - 1)
        except ValueError:
            print('Indice ínvalido')
    else:
        print('Não há livros para serem removidos')
    return bookcase


                        

        
#-------------------------------------------------------------------------------------------------------

bookcase = load_bookcase(FILE_JSON_PATH, Books) # Retorna lista de objetos

commands = {
    'cadastrar': lambda: bookcase.append(add_book()), #retorna um objeto e salva na lista
    'salvar': lambda: save_books(bookcase), #recebe uma lista de objetos e adiciona no json
    'carregar': lambda: load_bookcase(FILE_JSON_PATH, Books), #retorna lista de objetos
    'exibir': lambda: show_saved_books(bookcase), #imprime os livros cadastrados
    'deletar': lambda: del_book(bookcase) #retorna um lista de objetos
}

while True:
    

    menu_choice = input('Digite uma ação:')

    
    if menu_choice not in commands:
        print('Comando inválido')
        continue

    result = commands[menu_choice]()

    

    if result is not None:
        bookcase = result
    
    


   






#---------------------------------- MELHORIAS--------------------------------------------------------------
# tratar comando invalidos(numeros, numeros negativos, comando não encontrado, espaços vazios) OK
# melhorar a exibição do menu
# limpar a tela
# exibir mensagem confirmando carregar e avisando que dados não salvos serão perdidos