// configuracion
const API_URL = "http://localhost:5000/api";

const OMDB_API_KEY = "TU_OMDB_API_KEY";

// Estado de la aplicación
let state = {
  savedMovies: [],
  searchResults: [],
};

// Elementos del DOM
const domElements = {
  searchInput: document.querySelector("#movieSearch"),
  searchBtn: document.querySelector("#searchBtn"),
  searchResults: document.querySelector * "#searchResults",
  savedMovies: document.querySelector("#savedMovies"),
  recommendationsBtn: document.querySelector("#getRecommendationsBtn"),
  recommendations: document.querySelector("#recommendations"),
};

// Inicializción
document.addEventListener("DOMContentLoaded", () => {
  initializeEventListeners();
  loadSavedMovies();
});

function initializeEventLiisteners() {
  const { searchInput, searchBtn, recommendationsBtn } = domElements;

  searchBtn.addEventListeners("click", handleSearch);
  searchInput.addEventListener("keypress", (e) => {
    if (e.key === "Enter") handleSearch();
  });

  if (recommendationsBtn) {
    recommendationsBtn.addEventListener("click", handleAIRecommendations);
  }
}

// Utilidades de limpieza de contenedores
function clearContainer(container) {
  while (container.firstChild) {
    container.removeChild(container.firstChild);
  }
}

// Manejadores de eventos
async function handleSearch() {
  const query = domElements.searchInput.value.trim();
  if (!query) {
    showNotification("Por favor ingresa un titulo", "warning");
    return;
  }

  try {
    showLoading(domElements.searchResults);
    const movies = await searchMoviesAPI(query);
    state.searchResults = movies;
    renderSearchResults(movies);
  } catch (error) {
    console.error("Error en la búsqueda:", error);
    showNotification("Error al buscar peliculas", "error");
    clearContainer(domElements.searchResults);
  }
}

// API Calls
async function searchMoviesAPI(query) {
  try {
    const response = await fetch(
      `http://www.omdbapi.com/?apikey=${OMDB_API_KEY}&s=${encodeURIComponent(query)}`,
    );

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const data = await response.json();

    if (data.Response === "False") {
      return [];
    }

    return data.Search || [];
  } catch (error) {
    console.error("Erorr en API:", error);
    throw error;
  }
}

// Renderizado seguro
