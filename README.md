# 🎬IMDB API Movie People Finder
This web application connects to a cloud-hosted PostgreSQL database to retrieve and display IMDb movie data based on user-specified filters like rating threshold and adult content. It uses:
- A Python backend (FastAPI) for API logic and database handling.
- A JavaScript frontend (Node.js) that fetches and displays filtered results.
- A PostgreSQL database on the cloud, interfaced using SQLAlchemy ORM.

## Technology Used:
- ![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
- ![Node.js](https://img.shields.io/badge/Node.js-339933?style=for-the-badge&logo=node.js&logoColor=violet)
- ![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-FF6F00?style=for-the-badge&logo=sqlalchemy)
- ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=yellow)
- ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=lightblue)

## Modules:
### db_connection.py
This module manages all database interactions using SQLAlchemy ORM, including the definition of models for movies, ratings, and people. It establishes a connection to a cloud-hosted PostgreSQL database using credentials provided at runtime, processes and inserts normalized CSV data into relational tables, and provides query methods to filter movies by adult content, rating, and limit. It also includes helper functions for data cleaning, printing samples, and clearing tables.

### main.py
This FastAPI backend serves as the intermediary between the frontend and the database. It exposes two main endpoints: one to receive and store database credentials for establishing a connection, and another to return filtered movie data based on user input. The backend uses Pydantic models for input validation and maintains a persistent session for efficient database querying.

### mini_imdb_api.js
This Node.js script serves as a command-line frontend that interacts with the FastAPI backend. It reads database credentials from a local JSON file, establishes a connection to the backend, and then sends user-defined filters to retrieve movie data. The results are printed directly to the terminal, making it a simple interface for testing or integration.
