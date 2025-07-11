# Data-Science-Project
This is my first project done during training at Ansh Infotech
# 🎵 Spotify Song Recommender App

This is a **Streamlit web app** that recommends similar songs based on a user's input using Spotify song features such as energy, danceability, tempo, valence, and popularity. It uses **cosine similarity** to find and recommend the most similar tracks.

![App Screenshot](https://streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.png)

---

## 🚀 Live Demo

👉 [Click here to try the app](https://your-username-your-repo-name.streamlit.app)  
*(Replace with your actual Streamlit Cloud URL once deployed)*

---

## 📁 Project Structure


spotify-song-recommender/
│
├── app.py # Streamlit application script
├── Spotify_data.csv # Dataset containing song features
└── requirements.txt # Required Python packages


---

## 🔍 Features

- Enter a song name to receive top N similar tracks.
- Visual, interactive Streamlit UI.
- Uses audio features for similarity scoring:
  - Energy
  - Danceability
  - Tempo
  - Valence
  - Popularity

---

## 🧠 How It Works

1. Loads a dataset of Spotify songs with their audio features.
2. Normalizes the feature space using `StandardScaler`.
3. Computes **cosine similarity** between the selected song and all other songs.
4. Returns the top N most similar tracks.

---

## 🛠️ Tech Stack

- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [Pandas](https://pandas.pydata.org/)
- [Scikit-learn](https://scikit-learn.org/)

---

