import requests
import pandas as pd
search_term = ""
genius_search_url = "https://api.genius.com/search"
client_access_token = ""
headers = {"Authorization": f"Bearer {client_access_token}"}
songs = []

for page in range(1, 200): #Variar dependiendo de la cantidad de canciones que tenga el artista

    params = {"q": search_term, "page": page}
    response = requests.get(genius_search_url, headers=headers, params=params)
    json_data = response.json()
    hits = json_data["response"]["hits"]

    if not hits:
        break
    for song in hits:
        result = song["result"]
        songs.append({
            "song_id": result["id"],
            "song_name": result["title"],
            "genius_url": result["url"],
            "release_date":result["release_date_components"],
            "featured_artists":result["featured_artists"]
        })

    print(f"Página {page}: {len(hits)} canciones")

df = pd.DataFrame(songs)
df.to_csv("Dataset.csv", index=False)
print(f"\nTotal de canciones: {len(df)}")
