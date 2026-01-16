import logging

class Book:
    def __init__(self, title: str, author: str, year: int, isbn: str):
        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn
        self.is_borrowed = False
        
        # логируем создание книги
        logging.info(f"Создана книга: {title}, автор: {author}")
    
    def borrow(self):
        """Взять книгу"""
        self.is_borrowed = True
        logging.info(f"Книга '{self.title}' взята")
        return f"Книга '{self.title}' взята"
    
    def return_book(self):
        """Вернуть книгу"""
        self.is_borrowed = False
        logging.info(f"Книга '{self.title}' возвращена")
        return f"Книга '{self.title}' возвращена"