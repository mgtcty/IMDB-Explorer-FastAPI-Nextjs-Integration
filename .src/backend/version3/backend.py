import psycopg2
from configuration import config


# use for connecting to database and inserting query
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

        # determine if the query is for selecting data or inserting data
        if query.strip().upper().startswith("SELECT"):
            cursor.execute(query)
            highest_id = cursor.fetchone()[0]
        elif query.strip().upper().startswith("INSERT"):
            cursor.execute(query)

        # execute the insert command on the specified table
        cursor.close()
        
    # print the error if there are any
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    
    # close the connection    
    finally:
        if connection is not None:
            connection.close()
            print('Database connection terminated')

            # if the query was used for SELECT return the highest id
            if query.strip().upper().startswith("SELECT"):
                return highest_id


def get_actor_director(role):
    if role == 1:
        # get the highest id plus 1
        highest_actor_id = connect("SELECT person_id FROM stars ORDER BY person_id DESC LIMIT 1") + 1

        # debugging (remove if done)
        print("The retrieved person_id:", highest_actor_id)

        # return id
        return highest_actor_id
    else:
        # get the highest id plus 1
        highest_director_id = connect("SELECT person_id FROM directors ORDER BY person_id DESC LIMIT 1") + 1

        # debugging (remove if done)
        print("The retrieved person_id:", highest_director_id)

        # return id
        return highest_director_id


def insert_information(role, a_d_id, name, birth):
    # if an actor
    if role == 1:
        query_on_people = "INSERT INTO people (id, name, birth) VALUES ({},{},{})".format(a_d_id, name, birth)
        query_on_actors = "INSERT INTO actors (person_id) VALUES ({})".format(a_d_id)
        connect(query_on_people)
        connect(query_on_actors)
    # else is a director
    else:
        query_on_people = "INSERT INTO people (id, name, birth) VALUES ({},{},{})".format(a_d_id, name, birth)
        query_on_directors = "INSERT INTO directors (person_id) VALUES ({})".format(a_d_id)
        connect(query_on_people)
        connect(query_on_directors)
