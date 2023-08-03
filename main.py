class Library:
    def __init__(self):
        self.noBooks = 0
        self.books = []

    def addBook(self, book):
        self.books.append(book)
        self.noBooks = len(self.books)

    def showInfo(self):
        print(f"The library has {self.noBooks} books. The books are")
        for book in self.books:
            print(book)


l1 = Library()
l1.addBook("The Lord of the Rings by J.R.R. Tolkien")
l1.addBook("Harry Potter and the Philosopher’s Stone by J.K. Rowling")
l1.addBook("To Kill a Mockingbird by Harper Lee")
l1.addBook("Think and Grow Rich by Napoleon Hill")
l1.addBook("A Brief History of Time by Stephen Hawking")
l1.showInfo()

