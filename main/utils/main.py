from library.utils.library import Library


def main():
    try:
        lib = Library
        choice = input('выберите действие:'
                       '\n 1. Добавление книги;       4. отображение всех книг;'
                       '\n 2. Удаление книги;         5. Изменение статус книги;'
                       '\n 3. Поиск Книги;            6. Завершить программу.\n\n '
                       'Введите номер действия(например - 1): ').lower()

        if choice == '1':
            lib.add_book(input('Введите название книги: ').lower(), input('Введите автора книги: ').lower(),
                         input('Введите год издания книги: ').lower())

            main()
        if choice == '2':
            lib.delete_book(input('Введите id книги которую нужно удалить(например - 1): ').lower())
            main()
        if choice == '3':
            lib.search_book(input('Введите Название, автора или год издания книги: ').lower())
            main()
        if choice == '4':
            lib.all_books()
            main()
        if choice == '5':
            lib.switch_status_book(input('Введите id книги: ').lower(), input('Введите новый статус книги: ').lower())
            main()
        if choice == '6':
            return 0
        else:
            print(f'такого варианта выбора нет, попробуйте еще раз ')
            main()
    except KeyboardInterrupt:
        print('\n\nПрограмма завершена Оператором!')
