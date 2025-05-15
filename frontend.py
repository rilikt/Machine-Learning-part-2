import streamlit as st
import requests
import pandas as pd

# streamlit run frontend.py

st.title("YO!")

def load_genres():
    df = pd.read_csv("data/spotify_data.csv")
    genres = sorted(df["genre"].dropna().unique().tolist())
    return genres

genres = load_genres()
tempo = st.slider("Tempo (BPM)", 40.0, 220.0, 120.0)
duration = st.slider("Duration (seconds)", 30.0, 600.0, 180.0)
energy = st.slider("Energy", 0.0, 1.0, 0.5)
loudness = st.slider("Loudness (dB)", -60.0, 0.0, -10.0)
speechiness = st.slider("Speechiness", 0.0, 1.0, 0.05)
acousticness = st.slider("Acousticness", 0.0, 1.0, 0.5)
instrumentalness = st.slider("Instrumentalness", 0.0, 1.0, 0.0)
liveness = st.slider("Liveness", 0.0, 1.0, 0.2)
valence = st.slider("Valence", 0.0, 1.0, 0.5)
key = st.slider("Key (0 = C, 11 = B)", 0, 11, 0)
time_signature = st.selectbox("Time Signature", [3, 4, 5, 6, 7])
mode = st.radio("Mode (Major / Minor)", options=[True, False], format_func=lambda x: "Major" if x else "Minor")
genre = st.selectbox("Genre", genres)
year = 2025

features = {
    'energy': energy,
    'loudness': loudness,
    'speechiness': speechiness,
    'acousticness': acousticness,
    'instrumentalness': instrumentalness,
    'liveness': liveness,
    'valence': valence,
    'tempo': tempo,
    'duration': duration,
    'year': year,
    'genre': genre,
    'key': key,
    'time_signature': time_signature,
    'mode': mode,
}

response = requests.post("http://localhost:8000/predict", json=features)

if response.status_code == 200:
    prediction = response.json()
    st.write(prediction)
else:
    st.write("Something went wrong.")