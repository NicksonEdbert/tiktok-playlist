import time, os
import pandas as pd
from ytmusicapi import YTMusic, OAuthCredentials
from dotenv import load_dotenv

# Read from .env
load_dotenv()

# Fetch from .env
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

# 1. Authenticate with YouTube Music
print("Authenticating with YouTube Music...")
try:
    oauth_creds = OAuthCredentials(client_id, client_secret)
    ytmusic = YTMusic('oauth.json', oauth_credentials=oauth_creds)
    print("Authentication successful!")
except Exception as e:
    print("\nCould not authenticate. Did you run 'ytmusicapi setup'?")
    print(f"Error: {e}")
    exit()  # Exit the script if authentication fails

# 2. Load and Process Data (This part is identical)
print("Loading and processing song data...")
df = pd.read_csv('TikTok_songs_2022.csv')
top_songs_df = df.sort_values(by='track_pop', ascending=False)
top_30_songs = top_songs_df.head(30)

# 3. Iterate through the dataframe and search song's video ID on yt music.
videoID = []
for index, song in top_30_songs.iterrows():
    track_name = song['track_name']
    artist_name = song['artist_name']
    
    # A simple search query often works best
    query1 = f"{track_name} {artist_name}"

    # We add a small delay to be respectful to the API
    time.sleep(1) 

    searchResults = ytmusic.search(query=query1, filter='songs', limit=1)
    if searchResults:
        videoId = searchResults[0]['videoId']
        videoID.append(videoId)
        
        found_title = searchResults[0]['title']
        print(f"SUCCESS: Found '{found_title}' (ID: {videoId})")
    else:
        print(f"FAIL: Could not find '{track_name}' by {artist_name} on Youtube Music")

# 4. Create an empty playlist with playlist name and description
playlist_name = "Top TikTok Songs of 2022"
playlist_description = "A collection of the top TikTok songs from 2022, curated for your listening pleasure."
try:
    playlist_id = ytmusic.create_playlist(title=playlist_name, description=playlist_description, video_ids=videoID)
    print(f"Playlist '{playlist_name}' created successfully with ID: {playlist_id}")
except Exception as e:
    print(f"Can't create playlist")
    print(f"Error: {e}")
    playlist_id = None

# 5. Add the top 30 songs to the playlist

# You're done! Double check if everything is working