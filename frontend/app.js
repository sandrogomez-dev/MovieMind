// Configuracion 
const API_URL = 'http://localhost:5000/api';

// Estado de la aplicacion 
let savedMovies = [];

// Elementos del DOM
const searchInput = document.getElementById('movieSearch');
const searchBtn = document.getElementById('searchBtn');
const searchResults = document.getElementById('searchResults');
const savedMoviesContainer = document.getElementById('savedMovies');

// Event Listeners

searchBtn.addEventListener('click', searchMovies);
searchInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') searchMovies();
});

// Cargar peliculas guardadas al iniciar
loadSavedMovies();

// Funciones
async function searchMovies() {
    const query = searchInput.value.trim();
    if (!query) return;

    try {
        //Usar API de OMDB directamente
        const response = await fetch(`http://www.omdbapi.com/?apikey=TU_API_KEY&s=${query}`);
        const data = await response.json();

        if (data.Search) {
            displaySearchResults(data.Search);
        } else {
            searchResults.innerHTML = '<p class="no-results">No se encontraron resultados.</p>';
        }
    } catch (error){
        console.error('Error:', error);
        alert('Error al buscar peliculas');
    }
    }
    function displaySearchResults(movies) {
        searchResults.innerHTML = movies.map(movie => `
            <div class="movie-card">`)
    }
}

}