import os
import psycopg2
from psycopg2 import DatabaseError
from decouple import config


def get_connection():
    try:
        connection = psycopg2.connect(
                user=config('DB_USERNAME'),
                password=config('DB_PASSWORD'),
                host=config('DB_HOST'),
                port=config('DB_PORT'),
                database=config('DB_NAME')
        )
        return connection
    except DatabaseError as e:
        print(e)
        return None



# # Open a cursor to perform database operations
# cur = conn.cursor()

# # Execute a command: this creates a new table
# cur.execute('DROP TABLE IF EXISTS books;')
# cur.execute('CREATE TABLE books (id serial PRIMARY KEY,'
#                                  'title varchar (150) NOT NULL,'
#                                  'author varchar (50) NOT NULL,'
#                                  'pages_num integer NOT NULL,'
#                                  'review text,'
#                                  'date_added date DEFAULT CURRENT_TIMESTAMP);'
#                                  )

# # Insert data into the table

# cur.execute('INSERT INTO books (title, author, pages_num, review)'
#             'VALUES (%s, %s, %s, %s)',
#             ('A Tale of Two Cities',
#              'Charles Dickens',
#              489,
#              'A great classic!')
#             )


# cur.execute('INSERT INTO books (title, author, pages_num, review)'
#             'VALUES (%s, %s, %s, %s)',
#             ('Anna Karenina',
#              'Leo Tolstoy',
#              864,
#              'Another great classic!')
#             )

# conn.commit()

# cur.close()
# conn.close()