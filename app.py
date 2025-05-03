import streamlit as st

# Title
st.title("Moodify: Mood-focused Musicbox")
st.write("Tell us your mood, and we'll curate the perfect sound!")

# Mood Selection (with a blank first option)
mood_options = ["", "Happy", "Sad", "Whimsical"]
mood = st.selectbox("How are you feeling today?", mood_options)

# Playlist data matching mood options
music_data = {
    "Happy": {
        "title": "Feel Good Hits",
        "playlist": "https://open.spotify.com/playlist/51I0jlnjMG3CwWiPWenWbT?si=1df9f9407c2c4f55"
    },
    "Sad": {
        "title": "Let It All Out",
        "playlist": "https://open.spotify.com/playlist/6ipR6N8UnvtgRXoW1WKDA3?si=7deea8317c4a4172"
    },
    "Whimsical": {
        "title": "Forest Fairy Tunes",
        "playlist": "https://open.spotify.com/playlist/64yzaatRt8CU3KyF2lijPt?si=6d0f7bbc56194c66"
    }
}

# Show results only if a mood is selected
if mood != "":
    st.subheader(f"✮🎧 {music_data[mood]['title']} 🎧✮")
    st.markdown(f"[Click here to listen on Spotify]({music_data[mood]['playlist']})", unsafe_allow_html=True)