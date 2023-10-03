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


book1 = Book(1, "Mahabharata", "Vyasa", 1299, 5 )
book2 = Book(2, "Ramayana", "Valmiki", 1299, 5)

book1.info()
print("---------------\n ")
book2.info()


