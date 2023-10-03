class Book:
    def __init__(self, id, title, author, price, rating):
        self.id = id
        self.title = title
        self.author = author
        self.price = price 
        self.rating = rating

    def info(self):
        print(f"Book ID: {self.id}")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: {self.price}")
        print(f"Rating: {self.rating}")

class Books:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def find_by_id(self, id):
        for book in self.books:
            if book.id == id:
                return book
        return None
    
    def find_by_author(self, author):
        author_books = []
        for book in self.books:
            if book.author == author:
                author_books.append(book)
        return author_books
        
    def find_books_in_rating_range(self, min_rating, max_rating):
        rating_range_books = []
        for book in self.books:
            if book.rating >= min_rating and book.rating <= max_rating:
                rating_range_books.append(book)
        return rating_range_books
        
    def books_in_price_range(self, min_price, max_price):
        price_range_books = []
        for book in self.books:
            if book.price >= min_price and book.price <= max_price:
                price_range_books.append(book)
        return price_range_books
        

books = Books()

book1 = Book(1, "Mahabharata", "Vyasa", 11.0, 5 )
book2 = Book(2, "Ramayana", "Valmiki", 13.0, 5)
book3 = Book(3, "ABC" , "Vyasa", 12.0, 4.3)

books.add_book(book1)
books.add_book(book2)
books.add_book(book3)

found_book = books.find_by_id(2)
if found_book:
    print("Found book by ID: ")
    found_book.info()
else:
    print("Book not found by ID")

author_books = books.find_by_author("Vyasa")
if author_books:
    print("\nFound books by author: ")
    for book in author_books:
        book.info()
else:
    print("\n No books found by author")

rating_range_books = books.find_books_in_rating_range(4.5, 5.5)
if rating_range_books:
    print("\nFound books in the rating range:")
    for book in rating_range_books:
        book.info()
else:
    print("\nNo books found in the rating range")

price_range_books = books.books_in_price_range(10.0, 13.0)
if price_range_books:
    print("\nFound books in the price range: ")
    for book in price_range_books:
        book.info()
else:
    print("\nNo books found in the price range")



                
            

