from fastapi import FastAPI, HTTPException
from db_connection import DbConnection
from pydantic import BaseModel
import os
from dotenv import load_dotenv

app = FastAPI()

class Database_Selection(BaseModel):
    is_adult: int
    rating: float
    limit: int


GLOBAL_DB_CONNECTION = None

@app.on_event("startup")
def startup_event():
    access_db()

def access_db():
    '''
    Access the database given the credentials of the AWS RDS. Make sure that a connection with EC2 is running.
    '''
    # use credentials to access AWS RDS
    try:
        global GLOBAL_DB_CONNECTION
        load_dotenv()
        creds_data = {
            'user': os.getenv('user'),
            'password':os.getenv('password'),
            'database':os.getenv('database')
        }
        GLOBAL_DB_CONNECTION = DbConnection(creds_data)
        print("Database connection initialized.")
    except Exception as e:
        print("Error initializing DB connection:", e)

@app.get('/')
def root():
    return "Server Open"

@app.post('/get_movies_rating')
def get_movies_rating(item: Database_Selection):
    global GLOBAL_DB_CONNECTION
    data = GLOBAL_DB_CONNECTION.get_movies_data(item.is_adult, item.rating, item.limit)
    result = []
    print(data)
    print(type(data))
    for title, genres, rating in data:
        result.append({
            'title': title,
            'genres': genres,
            'rating': float(rating)
        })
    
    return {'data': result}
