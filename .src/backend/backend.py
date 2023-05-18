import psycopg2
from configuration import config


def connect(query):
    # initialize to nothing yet
    connection = None

    # try the lines of code as long as there is no error
    try: 
        # initialize parameters in the connection
        params = config()
        
        # connect to the database
        print('Connecting to the database...')
        connection = psycopg2.connect(**params)

        # initialize cursor
        cursor = connection.cursor()

        # get the max id
        cursor.execute('SELECT ')

        # execute the insert
        print('\n\nPostgreSQL database version: ')
        cursor.execute(query)
        cursor.close()
        
        # fetch the data on the database
        data = cursor.fetchone()
        print(data)
        '''for row in data:
            print(row)'''
        
    # print the error if there are any
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    
    # close the connection    
    finally:
        if connection is not None:
            connection.close()
            print('Database connection terminated')


connect('SELECT')
