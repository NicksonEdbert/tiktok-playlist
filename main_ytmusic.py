import panda as pd
from ytmusicapi import YTMusic

# 1. Authenticate with YouTube Music
# This looks for your headers_auth.json file
print("Authenticating with YouTube Music...")
try:
    ytmusic = YTMusic('headers_auth.json')
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

# 4. Create an empty playlist with playlist name and description

# 5. Add the top 30 songs to the playlist

# You're done! Double check if everything is working