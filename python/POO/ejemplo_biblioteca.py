class Library:
    def __init__(self):
        self.books = []
        self.users = []
    
    def add_book(self, book):
        self.books.append(book)
        print(f"el libro {book.title} ha sido agregado")
    
    def add_user(self, user):
        self.users.append(user)
        print(f"el ususario {user.name} ha sido registrado")
    
    def show_avalivable_book(self):
        print("los libros disponibles son:")
        for book in self.books:
            if book.avalivable:
                print(book.title)

class Book:
    def __init__(self, category,author, title):
        self.category = category
        self.author = author
        self.title = title
        self.avalivable = True
    
    def borrow(self):
        if self.avalivable:
            self.avalivable = False
            print(f"el libro {self.title} ha sido prestado")
        else:
            print(f"el libro {self.title} no esta disponible")

    def return_book(self):
        self.avalivable = True
        print(f"El libro {self.title} ha sido devuelto")

        

class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.avalivable:
            book.borrow()
            self.borrowed_books.append(book)
        else:
            print(f"El libro {book.title} no esta disponible")
        
    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
        else:
            print(f"El libro {book} ya no esta en la lista de libros porestados")

book1 = Book("suspense", "Stephen King", "It chapter 1")
book2 = Book("Magir realism", "Gabo", "Cien años de soledad")

user1 = User("tal", 1)

library1 = Library()
library1.add_book(book1)
library1.add_book(book2)
library1.add_user(user1)

library1.show_avalivable_book()
user1.borrow_book(book1)
library1.show_avalivable_book()
