class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn 
    
    def display_books(self):
        print('--Book Information--')
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"ISBN: {self.isbn}")

book_list = []

f = open('books.txt','r')
contents = f.readlines()

for content in contents:
    title, author, isbn = content.split(', ')

    books = Book(title,author, isbn)
    book_list.append(books)

f.close()

for book in book_list:
    book.display_books()