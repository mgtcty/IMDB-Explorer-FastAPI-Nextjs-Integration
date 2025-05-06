from sqlalchemy import create_engine, Column, Integer, Numeric, String, ForeignKey
from sqlalchemy.orm import Session, sessionmaker, relationship, declarative_base
import json
import pandas as pd

class Base(declarative_base):
    pass

class Movies(Base):
    __tablename__ = "Movies"
    tconst = Column(String, primary_key=True)
    movie_type = Column(String)
    primary_title = Column(String)
    original_title = Column(String)
    is_adult = Column(Integer)
    run_time_minute = Column(Integer)
    genres = Column(String)

    ratings = relationship("Ratings", back_populates="movie", cascade="all, delete-orphan")
    known_for = relationship('PeopleKnownForMovie',  back_populates='movie', cascade="all, delete-orphan")

class Ratings(Base):
    __tablename__ = "Ratings"
    tconst = Column(String, ForeignKey('Movies.tconst'))
    ave_rating = Column(Numeric)
    num_votes = Column(Integer)

    movie = relationship("Movies", back_populates="ratings")

class PeopleKnownForMovie(Base):
    __tablename__ = "PeopleKnownForMovie"
    nconst = Column(String, ForeignKey('Actors.nconst', 'Directors.nconst', 'Producers.nconst'))
    tconst = Column(String, ForeignKey('Movies.tconst'))
    role = Column(String)
    
    person = relationship("People", back_populates="known_for")
    movie = relationship("Movies", back_populates="known_for")

class People(Base):
    __tablename__ = "People"
    nconst = Column(String, primary_key=True)
    primary_name = Column(String)
    birth_year = Column(Integer)
    death_year = Column(Integer)
    known_for = relationship("PeopleKnownForMovie", back_populates="person", cascade="all, delete-orphan")

class DbConnection():
    def __init__(self, json_file):
        self.movies_df = None
        self.ratings_df = None
        self.people_df = None

        with open(json_file, "r") as file:
            self.data = json.load(file)

        if not self.data:
            raise Exception("No data found in json file")
        
        self.db_url = f"postgresql://{self.data['user']}:{self.data['password']}@{self.data['host']}:{self.data['port']}/{self.data['database']}"
        self.engine = create_engine(self.db_url)
        self.Session = sessionmaker(bind=self.engine)

    def database_insert(self, csv, content):
        # Normalize dataframe
        df = pd.read_csv(csv)
        self.normalize_csv_file(df, content)

        # Insert into the cloud database's table all initial dataframe
        self.insert_tables()

    def normalize_csv_file(self, df, content):
        if content == 'people':
            self.people_df = df.drop_duplicates(subset="nconst")
        elif content == 'movies':
            self.movies_df = df
        else:
            self.ratings_df = df

    def insert_tables(self):
        pass

connection = DbConnection('creds.json')

csv_files = [('csv/name.basics.normalized.csv', 'people'),('csv/title.basics.normalized.csv','movies'),('csv/title.ratings.csv','ratings')]

for csv, content in csv_files:
    connection.database_insert(csv, content)
