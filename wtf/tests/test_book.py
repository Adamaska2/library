#добавляем путь к папке wtf
import sys
sys.path.append('.')

#теперь импортируем
from src.models.book import Book

#простые тесты
def test_book_creation():
    book = Book("Книга", "Автор", 2024, "123")
    assert book.title == "Книга"
    print("Тест 1 прошел")

def test_book_info():
    book = Book("1984", "Оруэлл", 1949, "456")
    info = book.get_info()
    assert "1984" in info
    print("Тест 2 прошел")