import unittest
from library import Library

lib_test = Library()

TEST_TUPLE_1 = (
    ('души', 'Гоголь', '1835'),
    ('The Great Gatsby', 'Francis Scott Fitzgerald', '1925')
                )

TEST_TUPLE_2 = (
    ('Мертвые души', 'Гоголь', '-1'),
    ('The Great Gatsby', 'Francis Scott Fitzgerald', 'Это текст'),
    ('Мертвые души', 'Гоголь', '2055')
                )

TEST_TUPLE_3 = ('Мертвые души', 'Гоголь', '1835')

TEST_TUPLE_4 = ('Мстители', 'Райн Гослинг', '3035')

TEST_TUPLE_5 = (('1', 'выдана'), ('2', 'выдана'))

TEST_TUPLE_6 = (('3', 'Нету'), ('2', 'в наличии'))
TEST_1 = '1'


class Test_Lib_1(unittest.TestCase):
    def test_add_book_t(self):
        for tup in TEST_TUPLE_1:
            self.assertEqual(lib_test.add_book(tup[0], tup[1], tup[2]), True)

    def test_add_book_f(self):
        for tup in TEST_TUPLE_2:
            self.assertEqual(lib_test.add_book(tup[0], tup[1], tup[2]), False)


class Test_Lib_2(unittest.TestCase):
    def test_delete_book_t(self):
        lib_test.add_book('Мертвые души', 'Гоголь', '1835')
        self.assertEqual(lib_test.delete_book(TEST_1[0]), True)
        lib_test.all_books()

    def test_delete_book_f(self):
        self.assertEqual(lib_test.delete_book(TEST_1[0]), False)

    def test_search_book_t(self):
        lib_test.add_book('Мертвые души', 'Гоголь', '1835')
        for tup in TEST_TUPLE_3:
            self.assertEqual(lib_test.search_book(tup), None)

    def test_search_book_f(self):
        for tup in TEST_TUPLE_4:
            self.assertEqual(lib_test.search_book(tup), False)


class Test_Lib_3(unittest.TestCase):

    def test_all_books_t(self):
        lib_test.add_book('Мертвые души', 'Гоголь', '1835')
        self.assertEqual(lib_test.all_books(), None)

    def test_all_books_f(self):
        self.assertEqual(lib_test.all_books(), False)

    def test_switch_status_book_t(self):
        for tup in TEST_TUPLE_1:
            lib_test.add_book(tup[0], tup[1], tup[2])
        for tup_2 in TEST_TUPLE_5:
            self.assertEqual(lib_test.switch_status_book(tup_2[0], tup_2[1]), True)

    def test_switch_status_book_f(self):
        for tup in TEST_TUPLE_1:
            lib_test.add_book(tup[0], tup[1], tup[2])
            lib_test.all_books()
        for tup_2 in TEST_TUPLE_6:
            self.assertEqual(lib_test.switch_status_book(tup_2[0], tup_2[1]), False)








