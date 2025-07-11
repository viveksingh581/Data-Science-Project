import streamlit as st
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import StandardScaler

# Load your data
spotify_data = pd.read_csv("Spotify_data.csv")

# Preprocess features
features = spotify_data[['Energy', 'Danceability', 'Tempo', 'Valence', 'Popularity']]
scaler = StandardScaler()
features_scaled = scaler.fit_transform(features)

# Function to recommend songs
def recommend_songs(song_name, top_n=5):
    song_data = spotify_data[spotify_data['Track Name'].str.lower() == song_name.lower()]
    if song_data.empty:
        return ["Song not found in dataset."]
    song_index = song_data.index[0]
    similarity_scores = sorted(
        enumerate(cosine_similarity([features_scaled[song_index]], features_scaled)[0]),
        key=lambda x: x[1], reverse=True
    )
    top_songs = [spotify_data.iloc[i[0]]['Track Name'] for i in similarity_scores[1:top_n+1]]
    return top_songs

# Streamlit UI
st.title("🎵 Spotify Song Recommender")
st.write("Find songs similar to your favorite track!")

song_name = st.text_input("Enter a song name:")
top_n = st.slider("Number of recommendations:", 1, 10, 5)

if st.button("Recommend"):
    recommendations = recommend_songs(song_name, top_n=top_n)
    if recommendations[0] == "Song not found in dataset.":
        st.warning("❌ Song not found in dataset.")
    else:
        st.success("✅ Recommended Songs:")
        for i, song in enumerate(recommendations, 1):
            st.write(f"{i}. {song}")
