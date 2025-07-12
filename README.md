<p align="center">
  <img src="banner.png" alt="Movie Recommender App Banner" width="100%">
</p>

# 🎬 Movie Recommender App

A **Streamlit-based movie recommendation system** that suggests similar movies using **cosine similarity** and fetches movie posters using the **TMDB API**.

## 🚀 Demo

[Click here to try the live app]([https://hardeepsingh30-movie-recommender-app.streamlit.app](https://movie-recommender-app-25wvhjje4jbultxbicqei5.streamlit.app/))  
*(Replace with your actual Streamlit Cloud link)*

## 📌 Features

- Select a movie from the dropdown
- Get **5 similar movies** based on content similarity
- See movie **posters** using TMDB API
- Clean and responsive Streamlit UI

## 🧠 How It Works

- Precomputed similarity matrix using cosine similarity between movies
- TMDB API used to fetch posters based on movie title
- Uses `.pkl` files for fast loading of model data

## 🗂️ Project Structure
movie-recommender-app/
├── app1.py # Streamlit app
├── movie_titles.pkl # Movie titles list
├── similarity.pkl # Similarity matrix
├── movies.pkl # Optional movie metadata
├── file.tsv # Optional raw data
├── Movie_Id_Titles.csv # Optional ID-title mapping
├── Final Project.ipynb # Jupyter notebook for dev
├── requirements.txt # Dependencies



## 🔑 Setup (Local)

1. Clone the repo:
   ```bash
   git clone https://github.com/hardeepsingh30/movie-recommender-app.git
   cd movie-recommender-app
   
2. Install dependencies:
   pip install -r requirements.txt

3. Set TMDB API key
   In app1.py, replace:
     TMDB_API_KEY = st.secrets["TMDB_API_KEY"]

   Then create a .streamlit/secrets.toml file locally:
     TMDB_API_KEY = "your_actual_api_key_here"

4. Run the app:
   streamlit run app1.py
