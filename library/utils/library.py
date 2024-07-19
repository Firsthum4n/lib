import itertools
from custom_exeption.Custom_err import is_exist_ex


class Library:
    dict_of_books = {}
    cnt = itertools.count(1)

    class Book:
        def __init__(self, title: str, author: str, year: str) -> None:
            self.id = next(Library.cnt)
            self.title = title
            self.author = author
            self.year = year if int(year) < 2025 else print('none')
            self.status = 'в наличии'

    @classmethod
    def add_book(cls, title: str, author: str, year: str) -> bool:
        try:
            new_book = cls.Book(title, author, year)
            if int(year) > 2024 or int(year) < 1457:
                raise ValueError
            for key, value in cls.dict_of_books.items():
                for k, v in value.items():
                    if title == v:
                        raise is_exist_ex()
            else:
                cls.dict_of_books[f'{new_book.id}'] = {'Название': new_book.title, 'Автор': new_book.author,
                                                       'Год': new_book.year, 'Статус': new_book.status}
                return True
        except ValueError:
            print(f'{year} больше текущего года, меньше 1457 или вы вели текстовое значение попробуйте еще раз\n')
            return False
        except is_exist_ex:
            print('Такая книга уже есть в библиотеке')
            return False

    @classmethod
    def delete_book(cls, id: str) -> bool:
        try:
            del cls.dict_of_books[f'{id}']
            return True
        except KeyError:
            print(f'{id} - такго id нет\n')
            return False

    @classmethod
    def search_book(cls, request: str) -> [bool, None]:
        try:
            if len(cls.dict_of_books) != 0:
                for key, value in cls.dict_of_books.items():
                    for k, v in value.items():
                        if request == v:
                            print(cls.dict_of_books[key])
                            if not request == v:
                                raise ValueError

            else:
                raise KeyError
        except (ValueError, KeyError):
            print('Совпадений не найдено\n')
            return False

    @classmethod
    def all_books(cls) -> bool:
        try:
            if len(cls.dict_of_books) != 0:
                for book_key, book_value in cls.dict_of_books.items():
                    print(book_key, book_value)

            else:
                raise KeyError
        except KeyError:
            print('Библиотека пуста\n')
            return False


    @classmethod
    def switch_status_book(cls, id: str, new_status: str) -> bool:
        try:
            if (new_status != cls.dict_of_books[f'{id}']['Статус'] and
                    new_status == 'в наличии' or new_status == 'выдана'):
                cls.dict_of_books[f'{id}']['Статус'] = new_status
                return True
            else:
                raise ValueError
        except KeyError:
            print('Такого id нет\n')
            return False
        except ValueError:
            print('Статус равен текущему, либо указан некорреткный формат\n')
            return False
