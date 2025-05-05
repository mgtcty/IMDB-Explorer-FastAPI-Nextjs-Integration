from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
import json


class DbConnection:
    def __init__(self, json_file):
        with open(json_file, "r") as file:
            self.data = json.load(file)

        if not self.data:
            raise Exception("No data found in json file")
        
        print(self.data)
        
        self.db_url = f"postgresql://{self.data['user']}:{self.data['password']}@{self.data['host']}:{self.data['port']}/{self.data['database']}"
        self.engine = create_engine(self.db_url)

connection = DbConnection('creds.json')