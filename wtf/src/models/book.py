import pendulum


class Book:
    def __init__(self, title: str, author: str, year: int, isbn: str):
        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn
        self.added_date = pendulum.now("Europe/Moscow").to_date_string()

    def get_info(self) -> str:
        return f"{self.title}, автор - {self.author}, год издания - {self.year} (добавлена: {self.added_date})"


class EBook(Book):
    def __init__(self, title: str, author: str, year, format: str, isbn: str):
        super().__init__(title, author, year, isbn)
        self.format = format

    def get_info(self) -> str:
        return f"{self.title}, автор - {self.author}, год издания - {self.year}, формат - {self.format} (добавлена: {self.added_date})"
