class Library:
    def __init__(self, listOfBooks):
        self.available = listOfBooks

    def displayAvailableBooks(self):
        print()
        print("Available Books")
        for book in self.available:
            print(book)

    def lend(self, requestedbook):
        if self.requestedbook in self.available:
            print("You have now borrowed the book")
            self.available.remove(requestedbook)
        else:
            print("Sorry, that book is not available")

    def addBook(self, returnedBook):
        self.available.append(returnedBook)
        print("You have returned the book thank you")


class Customer:
    def request(self):
        print("What book would you like to borrow")
        self.book = input()
        return self.book

    def returnBook(self):
        print("What book would you like to return")
        self.returnedbook = input()
        return self.returnedbook

library = Library(["Think and Grow Rich", "Who Will Cry When You Die", "For One More Day"])
customer = Customer()
while True:
    print("Enter 1 to display the available books")
    print("Enter 2 to request a book")
    print("Enter 3 to return a book")
    print("Enter 4 to exit")
    userChoice = int(input())
    if userChoice == 1:
        library.displayAvailableBooks()
    elif userChoice == 2:
        requestedBook = customer.request()
        library.lend(requestedBook)
    elif userChoice == 3:
        returnedBook = customer.returnBook()
        library.addBook(returnedBook)
    elif userChoice == 4:
        quit()
