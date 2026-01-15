class Book:
    def __init__(self, title: str, author: str, year: int, isbn: str):
        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn
        self.is_borrowed = False  # новый атрибут
        
    def get_info(self) -> str:
        return f"{self.title}, автор - {self.author}, год издания - {self.year}"
    
    def borrow(self):
        """Взять книгу"""
        self.is_borrowed = True
        return f"Книга '{self.title}' взята"
    
    def return_book(self):
        """Вернуть книгу"""
        self.is_borrowed = False
        return f"Книга '{self.title}' возвращена"