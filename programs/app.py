import pyodbc as db
import utils
from dbutils import result_as_dict
from authors import *
from books import *
from reviews import *
from users import *



def main():
    driver = '{ODBC Driver 18 for SQL Server}'
    server = r'localhost\SQLEXPRESS'
    database = 'ecolabs_books_db'
    encrypt = 'no'
    trusted_Connection = 'yes'

    connection_string = f'''
        DRIVER={driver};
        SERVER={server};
        DATABASE={database};
        TRUSTED_CONNECTION={trusted_Connection};
        Encrypt={encrypt};

    '''

    with db.connect(connection_string) as connection:
        print('connection successful')
        print(type(connection))
        cursor = connection.cursor()
        print(type(cursor))
        print(cursor)

        command_mapping = {
            'get_all_authors': get_all_authors,
            'add_author': add_author,
            'remove_author': remove_author,
            'update_author': update_author,
            'get_author_review': get_author_review,
            'get_author_by_id': get_author_by_id,
            'get_book_by_id': get_book_by_id,
            'add_book_review': add_book_review,
            'get_book_review': get_book_review,
            'get_author_by_id': get_author_by_id,
            'get_all_books': get_all_books,
            'add_book': add_book,
            'remove_book': remove_book,
            'get_all_reviews': get_all_reviews,
            'add_new_user': add_new_user,
            'get_all_users': get_all_users,
            'get_user_review': get_user_review,
            'quit': exit,
            'exit': exit
        }

        while True:
            user_input = input('db> ')
            command_parts = user_input.split()
            if command_parts[0] in command_mapping:
                command_name = command_parts[0]
                arguments = command_parts[1:]
                
                if command_name == 'get_author_by_id' and not arguments:
                    id = input("Enter ID: ")
                    arguments = [id]
                
                
                 
                
                command_function = command_mapping[command_name]
                command_function(cursor, *arguments)
            else:
                print('Invalid command')



        # cursor.execute('select * from authors')

        # result = result_as_dict(cursor)
        
        # print(result)

        # rows = cursor.fetchall()
        # for row in rows:
        #     print(f'{row.title.ljust(50)}{row.author.ljust(50)}{str(row.price).ljust(10)}{str(row.rating).ljust(10)}')
        
        # result = cursor.execute('select * from book_summary');
        # print(f'result= {result}')
        # rows = cursor.fetchall()

        # for row in rows:
        #     for value in row:
        #         print(value, end='\t')
        #     print()




if __name__ == '__main__':
    main()


