import requests
import os


class Movie:
    """Model for logic related to movies."""

    @staticmethod
    def search_external(title):
        """Finding movies using an external API (e.g., OMDb)."""
        api_key = os.getenv('OMDB_API_KEY', 'your_api_key_here')
        url = f"http://www.omdbapi.com/?apikey={api_key}&t={title}"

        response = request.get(url)
        if response.status_code == 200:
            data = response.json()
            if data.get('Resposne') == 'True':
                return {
                    'title': data.get('Title'),
                    'year': data.get('Year'),
                    'poster': data.get('Poster'),
                    'rating': data.get('imdbRating', 0)
                }
        return None


class UserPreference:
    """Model for user related references"""

    @staticmethod
    def save_feedback(movie_id, liked, feedback_text=None):
        db = get_db()
        db.execute('INSER INTO user_preferences (movie_id, liked, feedback) VALUES (?, ?, ?)',
                   [movie_id, liked, feedback_text]
                   )
        db.commit()
