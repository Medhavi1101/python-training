from dbutils import result_as_dict


def add_book(cursor,book_id,title,book_details,author_id):
    cursor.execute('insert into Books(book_id,title,book_details,author_id) VALUES (?,?,?,?)',book_id,title,book_details,author_id)
    print(f'Book {title} added')


def get_all_books(cursor):
    cursor.execute("SELECT title FROM books")
    result = result_as_dict(cursor)
    print(result)


def get_book_by_id(cursor,book_id): 
    cursor.execute("SELECT * FROM books WHERE id = ?", (book_id,))
    result = cursor.fetchall()
    for book in result:
        print(book)

def remove_book(cursor,book_id):
    cursor.execute('DELETE FROM books WHERE id= ?', (book_id,))
    print("Book removed succesfully!!")


def get_book_review(cursor,book_id):
    cursor.execute('''SELECT B.title,B.details, R.rating, R.review_text 
                      FROM Reviews R
                      JOIN Books B ON R.bookid = B.bookid
                      WHERE R.reviewid = ?''',book_id)
    results=result_as_dict(cursor)
    for res in results:
            print(res)


def add_book_review(cursor,review_id,book_id,userid,rating,review_text):
    cursor.execute('insert into Reviews(review_id,book_id,userid,rating,review_text) VALUES (?,?,?,?,?)',review_id,book_id,userid,rating,review_text)
    print("Review added to the book")