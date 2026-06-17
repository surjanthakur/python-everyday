class Library:
    library_name = "NYC state 📚"
    def __init__(self):
        self.__all_books ={}
    
    def get_books(self):
        print(f"all books => {self.__all_books.items()}")

    def add_book(self , book:dict):
        self.__all_books.update(book)
        print("book added")

class Book:
    def __init__(self , book:dict):
        self.book = book


# insetation
p1 = Library()
b1 = Book({"james clear":"the automic habit"})

p1.add_book(b1.book)
p1.get_books()