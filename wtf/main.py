from src.models.book import Book
from src.models.user import User

book1 = Book("Виндзорские насмешницы", "Уильям Шекспир", 1597, "978-3-16-148410-0")
print(book1.get_info())

user = User(
    "Иван", "М", "+7 901-868-49-46", "'Виндзорские насмешницы', 'Джонни взял ружье'"
)
print(user.get_info())
