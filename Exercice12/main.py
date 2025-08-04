class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __repr__(self):
        return f"{self.title} de {self.author}({self.year})"


class Library:
    def __init__(self):
        self.books = []
        self.borrow_books = []

    def add_book(self, book: Book):
        self.books.append(book)

    def remove_book(self, book_title):
        for book in self.books:
            if book.title == book_title:
                self.books.remove(book)

    def borrow_book(self, book_title):
        for book in self.books:
            if book.title == book_title:
                self.borrow_books.append(book)
                self.remove_book(book_title)

    def return_book(self, book_title):
        for book in self.borrow_books:
            if book.title == book_title:
                self.add_book(book)
                self.borrow_books.remove(book)

    def available_books(self):
        print(self.books)
        return self.books

    def borrowed_books(self):
        print(self.borrow_books)
        return  self.borrow_books


if __name__ == "__main__":
    l = Library()
    b1 = Book("test","pierre","1992")
    b2 = Book("test2","yves","1956")
    b3 = Book("test3","isa","2012")

    l.add_book(b1)
    l.add_book(b2)
    l.add_book(b3)

    l.borrow_book(b2.title)
    l.borrow_book(b1.title)
    l.return_book(b2.title)
    l.available_books()
    l.borrowed_books()