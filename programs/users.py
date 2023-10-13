from dbutils import result_as_dict

def get_all_users(cursor):
    cursor.execute('select * from REVIEWS')
    results=result_as_dict(cursor)
    for res in results:
            print(res)

def add_new_user(cursor,id,name,password):
    cursor.execute('insert into Users (userid,username,password) values (?,?,?)',id,name,password)

def get_user_review(cursor,userid):
    cursor.execute('''SELECT R.userid,B.title, R.rating, R.review_text
                    FROM Reviews R
                    JOIN Books B ON R.bookid = B.bookid
                    WHERE R.userid = ?;''',userid)
    results=result_as_dict(cursor)
    for res in results:
            print(res)