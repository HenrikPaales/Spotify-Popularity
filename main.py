import sys
import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
from secret_envs import CID_code, SECRET_code, username_code, old_playlist_code, new_playlist_code

new_playlist_name = "ZERO Popularity"
popularity_limit = 0

CID = CID_code
SECRET = SECRET_code
username = username_code
scope = 'playlist-modify-private, playlist-read-private'

playlist_id = "1n5p8DGIPwR0rPVwhojajV"
new_playlist_id = "6ez21NrJp4ufFkmNeEQkU5"
token = util.prompt_for_user_token(username,
                           scope,
                           client_id=CID,
                           client_secret=SECRET,
                           redirect_uri='https://wikipedia.org')

sp = spotipy.Spotify(auth=token)


artist_names = []
track_names = []
popularitys = []
tids = []

playlist_id = old_playlist_code 
new_playlist_id = new_playlist_code
list_range = sp.playlist_tracks(playlist_id=playlist_id, fields="total")

playlist = sp.current_user_recently_played(limit=50)

for t in playlist["items"]:
    t = t["track"]
    artist_names.append(t["artists"][0]["name"])
    track_names.append(t["name"])
    tids.append(t["id"])
    popularitys.append(t["popularity"])

playlist_dataframe = pd.DataFrame({'tids' : tids, 'artist_name' : artist_names, 'track_name' : track_names, 'popularity' : popularitys})

print(playlist_dataframe.to_string())