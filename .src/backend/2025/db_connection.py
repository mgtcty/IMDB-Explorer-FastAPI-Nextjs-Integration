from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base, relationship
import json

class DbConnection():
    def __init__(self, json_file):
        with open(json_file, "r") as file:
            self.data = json.load(file)

        if not self.data:
            raise Exception("No data found in json file")
        
        self.db_url = f"postgresql://{self.data['user']}:{self.data['password']}@{self.data['host']}:{self.data['port']}/{self.data['database']}"
        self.engine = create_engine(self.db_url)

class Base(declarative_base):
    pass

class Movies(Base):
    pass

class Actors(Base):
    pass

connection = DbConnection('creds.json')