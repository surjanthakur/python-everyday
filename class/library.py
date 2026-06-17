class Book:
    def __init__(self , author:str , title:str):
        self.author  = author
        self.title = title
    
    def __str__(self):
        return f"author:{self.author} , book: {self.title}"

class Library:
    library_name = "NYC state 📚"

    def __init__(self):
        self.__all_books:list[Book] = []
    
    def get_books(self):
        return self.__all_books

    def add_book(self , book:Book):
        self.__all_books.append(book)

library = Library()

b1 = Book("James Clear", "Atomic Habits")
b2 = Book("Robert Kiyosaki", "Rich Dad Poor Dad")

library.add_book(b1)
library.add_book(b2)

for book in library.get_books():
    print(book)