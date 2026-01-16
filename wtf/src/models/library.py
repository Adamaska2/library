import logging
from .book import Book
from .user import User

class Library:
    def __init__(self):
        self.__books = {}
        self.__users = {}
        logging.info("Библиотека создана")
    
    def add_book(self, book: Book):
        """Добавить книгу"""
        self.__books[book.isbn] = book
        logging.info(f"Книга добавлена в библиотеку: {book.title}")
        return f"Книга '{book.title}' добавлена"
    
    def add_user(self, user: User):
        """Добавить пользователя"""
        self.__users[user.id_user] = user
        logging.info(f"Пользователь добавлен: {user.name}")
        return f"Пользователь '{user.name}' добавлен"
    