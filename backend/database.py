import sqlite3
import os

DATABASE_PATH = 'movies.db'


def get_db():
    """Get a connection to the database."""
    db = sqlite3.connect(DATABASE_PATH)
    db.row_factory = sqlite3.Row  # Enable access to columns by name
    return db


def init_db():
    # Initialize the database and create tables if they don't exist.
    db = get_db()

    # Movie table
    db.execute('''
               CREATE TABLE IF NOT EXISTS movies (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
               title TEXT NOT NULL,
               year INTEGER,
               poster TEXT,
               rating FLOAT DEFAULT 0,
               created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)
               ''')
    # Table for user preferences( AI recommendations)
    db.execute('''
               CREATE TABLE IF NOT EXISTS user_preferences (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   movie_id INTEGER,
                   liked BOOLEAN,
                   feedback TEXT,
                   created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                   FOREIGN KEY (movie_id) REFERENCES movies (id)
               )
               ''')

    db.commit()
    print("✅ Database initialized")
