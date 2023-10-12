from dbutils import result_as_dict

def get_all_authors(cursor):
    cursor.execute("SELECT author_name FROM authors")
    result = result_as_dict(cursor)
    print(result)

def get_author_by_id(cursor, id):
    cursor.execute("SELECT * FROM authors WHERE id = ?", (id,))
    result = cursor.fetchall()
    for author in result:
        print(author)

def add_author(cursor,author_id,author_name,bio):
    cursor.execute('insert into authors (author_id,author_name,bio) VALUES (?,?,?)',author_id,author_name,bio)
    print(f'{author_name} added')

def remove_author(cursor,id):
    cursor.execute('DELETE from authors where authorid=?',(id,))
    print(f'{id} deleted')

def update_author(cursor, author_id, new_author_name, new_bio):
    author_id = input("Enter author_id ID: ")
    cursor.execute(''' 
                   UPDATE authors 
                   SET author_name = ?, 
                   bio = ? 
                   where author_id = ?, 
                   ''', (new_author_name, new_bio))
    
def get_author_review(cursor,author_id):
    cursor.execute('''SELECT B.title, R.rating, R.review_text 
                      FROM Reviews R
                      JOIN Books B ON R.bookid = B.bookid
                      WHERE B.authorid = ?''',author_id)
    results=result_as_dict(cursor)
    for res in results:
            print(res)