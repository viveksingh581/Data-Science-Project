# Data-Science-Project
This is my first project done during training at Ansh Infotech Pvt. Ltd. In this project first I learn to visualize the data insights like music popularity from the spotify dataset which includes song features i.e. 'Energy', 'Valence', 'Danceability', 'Loudness', 'Acousticness' Using these features the popularity graph Matplot, Seaborn, Histgram chart is created to predict popularity of tracks with the healp of sklearn metrics.
# 🎵 Spotify Song Recommender App

This is a **Streamlit web app** that recommends similar songs based on a user's input using Spotify song features such as energy, danceability, tempo, valence, and popularity. It uses **cosine similarity** to find and recommend the most similar tracks.

![App Screenshot]<img width="1262" height="847" alt="Screenshot 2025-07-11 120557" src="https://github.com/user-attachments/assets/759936c9-c275-408c-b0c8-53252bbde4d4" />

<img width="1203" height="894" alt="Screenshot 2025-07-11 120630" src="https://github.com/user-attachments/assets/f5867670-66fd-4375-ae15-7fc0072858dd" />

---

## 🚀 Live Demo

👉 [Click here to try the app](https://data-science-project-zhbspmuu2zch4utmtzkzti.streamlit.app/)  


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

