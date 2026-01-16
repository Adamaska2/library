import logging

class User:
    id_counter = 1
    
    def __init__(self, name: str, gender: str, phone: str):
        self.id_user = User.id_counter
        User.id_counter += 1
        self.name = name
        self.gender = gender
        self.phone = phone
        self.books = []
        
        logging.info(f"Создан пользователь: {name}, ID: {self.id_user}")
    
    def borrow_book(self, book):
        """Взять книгу"""
        self.books.append(book)
        book.borrow()
        logging.info(f"Пользователь {self.name} взял книгу '{book.title}'")
        return f"Пользователь {self.name} взял книгу '{book.title}'"