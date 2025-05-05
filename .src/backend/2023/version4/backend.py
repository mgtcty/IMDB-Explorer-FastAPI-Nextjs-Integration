import psycopg2
from configuration import config


# use for connecting to database and inserting query
def connect(query, values):
    # initialize to nothing yet
    print(values)
    connection = None

    # try the lines of code as long as there is no error
    try: 
        # initialize parameters in the connection
        params = config()
        
        # connect to the database
        connection = psycopg2.connect(**params)

        # initialize cursor
        cursor = connection.cursor()

        # determine if the query is for selecting data or inserting data
        if query.strip().upper().startswith("SELECT"):
            cursor.execute(query)
            highest_id = cursor.fetchone()[0]
        elif query.strip().upper().startswith("INSERT"):
            cursor.execute(query, values)
            connection.commit()

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
        highest_actor_id = connect("SELECT person_id FROM stars ORDER BY person_id DESC LIMIT 1", None) + 1

        # debugging (remove if done)
        print("The retrieved person_id:", highest_actor_id)

        # return id
        return highest_actor_id
    else:
        # get the highest id plus 1
        highest_director_id = connect("SELECT person_id FROM directors ORDER BY person_id DESC LIMIT 1", None) + 1

        # debugging (remove if necessary)
        print("The retrieved person_id:", highest_director_id)

        # return id
        return highest_director_id


def get_highest_movie_id():
    movie_id = connect('SELECT * FROM movies ORDER BY id DESC LIMIT 1', None) + 1

    # debugging (remove if necessary)
    print("The retrieved movie_id:", movie_id)

    # return id
    return movie_id


def insert_information(role, a_d_id, name, movie_id, movie_name, ratings, votes, movie_year, birth):
    # if an actor
    if role == 1:
        # make the query
        queries = {
            "INSERT INTO people (id, name, birth) VALUES (%s,%s,%s)": (a_d_id, name, birth),
            "INSERT INTO movies (id, title, year) VALUES (%s,%s,%s)": (movie_id, movie_name, movie_year),
            "INSERT INTO stars (person_id, movie_id) VALUES (%s, %s)": (a_d_id, movie_id),
            "INSERT INTO ratings (movie_id, rating, votes) VALUES (%s, %s, %s)": (movie_id, ratings, votes)
        }

        # execute the queries
        for query_name, query in queries.items():
            print(query_name, " : ", query)
            connect(query_name, query)
    # else is a director
    else:
        # make the query
        queries = {
            "INSERT INTO people (id, name, birth) VALUES (%s,%s,%s)": (a_d_id, name, birth),
            "INSERT INTO movies (id, title, year) VALUES (%s,%s,%s)": (movie_id, movie_name, movie_year),
            "INSERT INTO directors (person_id, movie_id) VALUES (%s, %s)": (a_d_id, movie_id),
            "INSERT INTO ratings (movie_id, rating, votes) VALUES (%s, %s, %s)": (movie_id, ratings, votes)
        }

        # execute the queries
        for query_name, query in queries.items():
            print(query_name, " : ", query)
            connect(query_name, query)
