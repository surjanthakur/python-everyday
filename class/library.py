class Library:
    library_name = "NYC state 📚"
    def __init__(self):
        self.__all_books =[]
    
    def get_books(self):
        print(f"all books => {self.__all_books.items()}")

    def add_book(self , book:dict):
        self.__all_books.update(book)
        print("book added")

class Book:
    def __init__(self , author:str , title:str):
        self.author  = author
        self.title = title