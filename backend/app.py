from flask import Flask, request, jsonify
from flask_cors import CORS
from database import init_db, get_db
from models import Movie, UserPreference
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Initialize the database

init_db()


@app.route('/health', methods=['GET'])
def health_check():
    """Endpoint to check if the server is running."""
    return jsonify({"status": "ok", "message": "Server is running!"})


@app.route('/api/movies', methods=['GET'])
def get_movies():
    """Endpoint to get a list of movies."""
    db = get_db()
    cursor = db.execute('SELECT * FROM movies ORDER BY created_at DESC')
    movies = cursor.fetchall()

    # Convertir a lista de diccionarios.
    movies_list = []
    for movie in movies:
        movies_list.append({
            'id': movie['id'],
            'title': movie['title'],
            'year': movie['year'],
            'poster': movie['poster'],
            'rating': movie['rating']

        })

        return jsonify(movies_list)


@app.route('/api/movies', methods=['POST'])
def add_movie():
    """Save a new movie to the database."""
    data = request.json

    db = get_db()
    cursor = db.execute('INSERT INTO movies (title,year,poster,rating) VALUES(?,?,?,?)', [
                        data['title'], data['year'], data['poster'], data.get('rating', 0)])
    db.commit()

    return jsonify({"message": "Movie added successfully!"}), 201


if __name__ == '__main__':
    app.run(debug=True, port=5000)
