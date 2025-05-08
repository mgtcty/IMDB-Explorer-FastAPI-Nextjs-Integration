from fastapi import FastAPI, HTTPException
from db_connection import DbConnection
from pydantic import BaseModel

app = FastAPI()

class Database_Creds(BaseModel):
    user:str
    password:str
    database:str

class Database_Selection(BaseModel):
    is_adult: int
    rating: float
    limit: int


GLOBAL_CONNECTION = None

@app.get('/')
def root():
    return "Access Db"

@app.post('/access_db')
def access_db(creds: Database_Creds):
    try:
        global GLOBAL_CONNECTION
        creds_data = {
            'user': creds.user,
            'password':creds.password,
            'database':creds.database
        }
        GLOBAL_CONNECTION = DbConnection(creds_data)
        return {'Status': 'Connected'}
    except Exception as e:
        return {
                'Status': 'Not Connected. Check credentials: user, password, database',
                'Error': e
            }

@app.post('/get_movies_rating')
def get_movies_rating(item: Database_Selection):
    global GLOBAL_CONNECTION
    data = GLOBAL_CONNECTION.get_movies_rating(item.is_adult, item.rating, item.limit)
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

    

