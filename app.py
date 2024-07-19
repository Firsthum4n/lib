import itertools
import json


class Library:
    dict_of_books = {}
    cnt = itertools.count(1)

    class Book:
        def __init__(self, title, author, year):
            self.title = title
            self.author = author
            self.year = year
            self.status = 'в наличии'

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
        cls.dict_of_books[f'id{id}']['Статус'] = new_status


def main():
    lib = Library
    choice = input('выберите действие:\n 1. Добавление книги;\n 2. Удаление книги;\n 3. Поиск Книги;\n '
                   '4. отображение всех книг;\n 5. Изменение статус книги;\n 6. Завершить программу.\n Введите номер действия(например - 1): ').lower()
    if choice == '1':
        lib.add_book(input('Введите название книги: '), input('Введите автора книги: '), input('Введите год издания книги: '))
        main()
    if choice == '2':
        lib.delete_book(input('Введите id книги которую нужно удалить(например - 1): '))
        main()
    if choice == '3':
        lib.search_book(input('Введите Название, автора или год издания книги: '))
        main()
    if choice == '4':
        lib.all_books()
        main()
    if choice == '5':
        lib.switch_status_book(input('Введите id книги: '), input('Введите новый статус книги: '))
        main()
    if choice == '6':
        return 0


if __name__ == '__main__':
    main()








#
# lib.add_book('Мертвые души', 'Гоголь', 1835)
# lib.add_book('ccc', 'vvv', 1888)
# lib.add_book('Живые души', 'Гоголь', 1835)
#
#
# lib.switch_status_book('id3', 'выдана')
#
# lib.all_books()
#


