class Book:
    def __init__(self, title: str, author: str, year: int, pages: int, isbn: str):
        self.title = title
        self.author = author
        self.year = year
        self.pages = pages
        self.isbn = isbn

    def __str__(self) -> str:
        return f"Книга: '{self.title}', автор — {self.author}, год публикации — {self.year}"

book1 = Book("Название", "Автор", 1990, 301, "978-985-577-957-6")
print(book1)