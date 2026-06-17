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
    
    def show_books(self):
        return self.__all_books

    def add_book(self , book:Book):
        self.__all_books.append(book)
    
    def search_book(self , query:str):
        for book in self.__all_books:
            if book.author.strip().lower() ==  query.strip().lower() or book.title.strip().lower() ==  query.strip().lower() :
                return book
            else:
                print("cannot find book")
                
    def borrow_book(self , book_name:str):
        for book in self.__all_books:
            if book.title.strip().lower() == book_name.strip().lower():
                self.__all_books.remove(book)
                print(f"you borowed book: {book.title} by {book.author}")
                return book
            else:
                print("cannot find book")

library = Library()

b1 = Book("James Clear", "Atomic Habits")
b2 = Book("Robert Kiyosaki", "Rich Dad Poor Dad")

library.add_book(b1)
library.add_book(b2)

print(library.search_book("Rich Dad Poor Dad"))