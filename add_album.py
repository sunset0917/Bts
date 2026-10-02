from  lyricsgenius import Genius
import pandas as pd

client_access_token = ""
genius = Genius(client_access_token)
df = pd.read_csv("")
albums = []
song_id = df["song_id"].to_list()

for num_id in song_id:
    data = genius.song(num_id)

    try:
        album_name = data["song"]["album"]["name"]
    except (KeyError, TypeError):
        album_name = ""
    #rint(album_name)
    albums.append(album_name)

df["album"] = albums
df.to_csv("", index=False)

