import itertools
import json


class Library:
    dict_of_books = {}
    dict_of_books = json.dumps(dict_of_books)
    cnt = itertools.count(1)

    class Book:
        def __init__(self, title, author, year):
            self.title = title
            self.author = author
            self.year = year
            self.status = 'в налчии'

    @classmethod
    def add_book(cls, title, author, year):

        new_book = cls.Book(title, author, year)
        cls.dict_of_books[f'id{next(cls.cnt)}'] = {'Название': new_book.title, 'Автор': new_book.author,
                                                   'Год': new_book.year, 'Статус': new_book.status}

    @classmethod
    def delete_book(cls, id):
        del cls.dict_of_books[f'id{id}']

    @classmethod
    def search_book(cls, request):
        for key, value in cls.dict_of_books.items():
            for k, v in value.items():
                if request == v:
                    print(cls.dict_of_books[key])

    @classmethod
    def all_books(cls):
        for book_key, book_value in cls.dict_of_books.items():
            print(book_key, book_value)

    @classmethod
    def switch_status_book(cls, id, new_status):
        cls.dict_of_books[id]['Статус'] = new_status



lib = Library

lib.add_book('Мертвые души', 'Гоголь', 1835)
lib.add_book('ccc', 'vvv', 1888)
lib.add_book('Живые души', 'Гоголь', 1835)


lib.switch_status_book('id3', 'выдана')

lib.all_books()



