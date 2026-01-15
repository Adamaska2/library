class User:
    # cтатическая переменная для id
    id_counter = 1

    def __init__(self, name: str, gender: str, phone: str, borrow_history: str = ""):
        self.id_user = User.id_counter  # уникальный ID
        User.id_counter += 1

        self.name = name
        self.gender = gender
        self.phone = phone
        self.borrow_history = borrow_history
        self.books = []  # список взятых книг

    def get_info(self) -> str:
        return f"{self.name} (ID: {self.id_user}), пол - {self.gender}, телефон - {self.phone}"

    def borrow_book(self, book):
        """Взять книгу"""
        self.books.append(book)
        book.borrow()
        return f"Пользователь {self.name} взял книгу '{book.title}'"

    def return_book(self, book):
        """Вернуть книгу"""
        if book in self.books:
            self.books.remove(book)
            book.return_book()
            return f"Пользователь {self.name} вернул книгу '{book.title}'"
        return "Книга не найдена"
