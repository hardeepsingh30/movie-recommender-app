import streamlit as st
import joblib
import requests

# Load data
movie_titles = joblib.load('movie_titles.pkl')
similarity = joblib.load('similarity.pkl')

# Banner image (if hosted or uploaded locally)
st.image("banner.png", use_container_width=True)

# Title & Intro
st.markdown("# 🎬 Movie Recommender System")
st.markdown("##### *Discover similar films instantly using AI + TMDB API*")

# Sidebar
st.sidebar.title("📽️ About This App")
st.sidebar.info(
    """
    This app recommends 5 similar movies based on your selection using
    cosine similarity & TMDB API.

    **Built with ❤️ by Hardeep Singh**
    """
)

# TMDB API
TMDB_API_KEY = "YOUR_REAL_API_KEY"

# Fetch poster using TMDB Search API (by title)
def fetch_poster(movie_title):
    url = f"https://api.themoviedb.org/3/search/movie?api_key={TMDB_API_KEY}&query={movie_title}"
    response = requests.get(url)
    data = response.json()

    if data.get("results"):
        poster_path = data["results"][0].get("poster_path")
        if poster_path:
            return "https://image.tmdb.org/t/p/w500/" + poster_path

    return "https://via.placeholder.com/300x450?text=No+Poster"

# Recommend function
def recommend(movie):
    if movie not in similarity.columns:
        st.error("Movie not found in similarity matrix.")
        return [], []

    similar_scores = similarity[movie].sort_values(ascending=False)[1:6]
    recommended_movies = similar_scores.index.tolist()
    recommended_posters = [fetch_poster(name) for name in recommended_movies]
    return recommended_movies, recommended_posters

# Search bar
search = st.text_input("🔍 Search for a movie:")
filtered_movies = [m for m in similarity.columns if search.lower() in m.lower()]
movie_list = list(similarity.columns)
selected_movie = st.selectbox("Choose a movie:", filtered_movies if search else movie_list)

# Button
if st.button("🎥 Recommend"):
    names, posters = recommend(selected_movie)

    if names:
        cols = st.columns(5)
        for col, name, poster in zip(cols, names, posters):
            with col:
                st.image(poster)
                st.caption(name)
