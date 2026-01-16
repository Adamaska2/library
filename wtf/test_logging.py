import logging
from src.models.book import Book
from src.models.user import User
from src.models.library import Library

# Настройка логирования
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(message)s',
    filename='test.log'
)

print("=== Тест логирования ===")

# Тестируем
book = Book("Тестовая книга", "Автор", 2024, "123")
user = User("Иван", "М", "+7 999 123-45-67")
library = Library()

library.add_book(book)
library.add_user(user)
user.borrow_book(book)
book.return_book()

print("Логи записаны в test.log")