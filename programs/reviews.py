from dbutils import result_as_dict


def get_all_reviews(cursor):
    cursor.execute('select * from reviews')
    results=result_as_dict(cursor)
    for res in results:
            print(res)