from sqlalchemy import create_engine, Column, Integer, Numeric, String, ForeignKey, func
from sqlalchemy.orm import Session, sessionmaker, relationship, declarative_base
import json
import pandas as pd

Base = declarative_base()

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
    id = Column(Integer, primary_key=True, autoincrement=True)
    tconst = Column(String, ForeignKey('Movies.tconst'))
    ave_rating = Column(Numeric)
    num_votes = Column(Integer)

    movie = relationship("Movies", back_populates="ratings")

class PeopleKnownForMovie(Base):
    __tablename__ = "PeopleKnownForMovie"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nconst = Column(String, ForeignKey('People.nconst'))
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
    def __init__(self, data):
        self.movies_df = None
        self.ratings_df = None
        self.people_df = None
        self.people_known_for_movies_df = None
        self.data = data

        if not self.data:
            raise Exception("Invalid credentials. Check password, database, and username.")
        
        # Access the AWS RDS using credentials of the user
        self.db_url = f"postgresql://{self.data['user']}:{self.data['password']}@localhost:15432/{self.data['database']}"
        self.engine = create_engine(self.db_url)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    def database_insert_initial_data(self, csv_files):
        # Normalize dataframe
        for csv, content in csv_files:
            df = pd.read_csv(csv)
            self.normalize_csv_file(df, content)

        # Insert into the cloud database's table all initial dataframe
        self.insert_tables()

    def normalize_csv_file(self, df, content):
        if content == 'people':
            self.people_df = df.drop_duplicates(subset="nconst")
            self.people_known_for_movies_df = df[['nconst', 'primaryProfession', 'knownForTitles']]
        elif content == 'movies':
            self.movies_df = df
        else:
            self.ratings_df = df

    def clean(self, value):
        return None if pd.isna(value) or value == r'\N' else value

    def insert_tables(self):
        self._bulk_insert(
            self.people_df,
            People,
            {
                "nconst": "nconst",
                "primary_name": "primaryName",
                "birth_year": "birthYear",
                "death_year": "deathYear"
            }
        )
        print('\tDone inserting People')

        self._bulk_insert(
            self.movies_df,
            Movies,
            {
                "tconst": "tconst",
                "movie_type": "titleType",
                "primary_title": "primaryTitle",
                "original_title": "originalTitle",
                "is_adult": "isAdult",
                "run_time_minute": "runtimeMinutes",
                "genres": "genres"
            }
        )

        self._bulk_insert(
            self.people_known_for_movies_df,
            PeopleKnownForMovie,
            {
                "nconst": "nconst",
                "tconst": "knownForTitles",
                "role": "primaryProfession"
            }
        )

        self._bulk_insert(
            self.ratings_df,
            Ratings,
            {
                "tconst": "tconst",
                "ave_rating": "averageRating",
                "num_votes": "numVotes"
            }
        )

    def _bulk_insert(self, df, model_class, field_map, batch_size=1000):
        buffer = []
        try:
            for index, row in df.iterrows():
                kwargs = {}
                for model_field, src_field in field_map.items():
                    val = row[src_field]
                    if pd.isna(val) or val == r"\N":
                        val = None
                    kwargs[model_field] = val

                buffer.append(model_class(**kwargs))

                if len(buffer) == batch_size:
                    self.session.bulk_save_objects(buffer)
                    self.session.commit()
                    buffer = []

            if buffer:
                self.session.bulk_save_objects(buffer)
                self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e
        
    def delete_all_data(self):
        to_delete = input("Are you sure you want to delete(yes/no)? ")
        if to_delete in ['y','Y','yes', 'ye']:
            self.session.query(People).delete()
            self.session.query(Movies).delete()
            self.session.commit()
        else:
            print("Action cancelled.")
        
    def print_sample_data(self):
        print("=== People ===")
        for person in self.session.query(People).limit(5):
            print(person.nconst, person.primary_name, person.birth_year)

        print("\n=== Movies ===")
        for movie in self.session.query(Movies).limit(5):
            print(movie.tconst, movie.primary_title, movie.genres, movie.movie_type, movie.is_adult)

        print("\n=== Ratings ===")
        for rating in self.session.query(Ratings).limit(5):
            print(rating.tconst, rating.ave_rating, rating.num_votes)

        print("\n=== PeopleKnownForMovie ===")
        for known in self.session.query(PeopleKnownForMovie).limit(5):
            print(known.nconst, known.tconst, known.role)
    
    # TODO: Further refine the reading of data, initially capable of two tables only
    def get_movies_rating(self, is_adult, rating, limit):
        result = self.session.query(
            Movies.primary_title,
            Movies.movie_type,
            Movies.genres,
            Ratings.ave_rating
        ).join(Ratings, Ratings.tconst == Movies.tconst).filter(Movies.is_adult == is_adult and Ratings.ave_rating > rating).order_by(Ratings.ave_rating.desc()).limit(limit).all()

        return result


'''csv_files = [('csv/filtered_people.csv', 'people'),('csv/filtered_movies.csv', 'movies'),('csv/filtered_ratings.csv', 'ratings') ]
with open('creds.json', "r") as file:
    data = json.load(file)
connection = DbConnection(data)
#connection.database_insert_initial_data(csv_files)
connection.print_sample_data()
#connection.delete_all_data()'''
