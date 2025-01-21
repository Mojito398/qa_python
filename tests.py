import pytest

from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    def test_add_new_book_with_invalid_name_length(self):
        collector = BooksCollector()
        collector.add_new_book('')
        collector.add_new_book('A' * 41)
        assert len(collector.get_books_genre()) == 0

    def test_set_book_genre_valid(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        assert collector.get_book_genre('Гордость и предубеждение и зомби') == 'Фантастика'

    def test_set_book_genre_invalid_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Несуществующий жанр')
        assert collector.get_book_genre('Гордость и предубеждение и зомби') == ''

    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Книга 1')
        collector.add_new_book('Книга 2')
        collector.set_book_genre('Книга 1', 'Фантастика')
        collector.set_book_genre('Книга 2', 'Ужасы')
        assert collector.get_books_with_specific_genre('Фантастика') == ['Книга 1']

    @pytest.mark.parametrize(
        'book_name, genre, expected_books',
        [
            ('Книга 1', 'Фантастика', ['Книга 1']),
            ('Книга 2', 'Ужасы', []),  # Жанр с возрастным рейтингом
            ('Книга 3', 'Мультфильмы', ['Книга 3']),
        ]
    )
    def test_get_books_for_children(self, book_name, genre, expected_books):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_books_for_children() == expected_books

    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Книга 1')
        collector.add_book_in_favorites('Книга 1')
        assert 'Книга 1' in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_twice(self):
        collector = BooksCollector()
        collector.add_new_book('Книга 1')
        collector.add_book_in_favorites('Книга 1')
        collector.add_book_in_favorites('Книга 1')
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Книга 1')
        collector.add_book_in_favorites('Книга 1')
        collector.delete_book_from_favorites('Книга 1')
        assert 'Книга 1' not in collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        collector.add_new_book('Книга 1')
        collector.add_new_book('Книга 2')
        collector.add_book_in_favorites('Книга 1')
        collector.add_book_in_favorites('Книга 2')
        assert collector.get_list_of_favorites_books() == ['Книга 1', 'Книга 2']