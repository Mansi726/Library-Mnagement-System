#library class
    #book display
    #lend book
    #add book
   # return book
   #dic=who owns the book if not present key=books,value=name
   #using class make library harry library=library(list of books,libr name,)
#create main and ifinite loop asking for input
class Library:
    def __init__(self,list_books,library_name):
        self.list_books=list_books
        self.library_name=library_name
        self.lend_data={}



    def display(self):
        for books in self.list_books:
                print(books)

    def lend_book(self,books,reader):
        if books in self.list_books:

                self.lend_data[books]=reader
                print('Book lend')
                self.list_books.remove(books)

        else:
                print('You have entered a wrong book or book lended')


    def add_book(self,book_name):
        self.list_books.append(book_name)

    def return_book(self,book_name):
        self.list_books.append(book_name)

def hey():
    list_books = ['Science', 'Maths', 'Social', 'Hindi', 'Humanities']
    library_name = 'Harry'
    Harry = Library(list_books,library_name)
    print('Welcome to my library')
    m=input("Enter f for moving forward \nEnter q for Exit:")
    while (m=='f'):
        ch = input( 'Enter A for adding a book \nEnter L for lending a book \nEnter R for returning a book \n Enter D for display:')

        if ch=='A':
            b=input("Enter book name:")
            Harry.add_book(b)
        elif ch=='L':
            l=input('Enter book name:')
            r=input('Enter reader name:')
            Harry.lend_book(l,r)
        elif ch=='R':
            rt=input('Enter book name:')
            Harry.return_book(rt)
        elif ch=='D':
            Harry.display()
hey()