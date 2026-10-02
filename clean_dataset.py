import pandas as pd
import ast

def parsear_fecha_diccionario(x):
    # Si es un valor nulo real (float o None), devolvemos NaT (Not a Time)
    if pd.isna(x):
        return pd.NaT
    try:
        # Convertimos el string a un diccionario real
        datos = ast.literal_eval(str(x))
        # Creamos la fecha usando los datos del diccionario
        return pd.Timestamp(year=datos["year"], month=datos["month"], day=datos["day"])
    
    except (ValueError, SyntaxError, TypeError, KeyError):
        # Si el string está mal formado, le falta una clave o da error, hace "pass" y devuelve NaT
        return pd.NaT
    
df = pd.read_csv("Dataset_bts_completo.csv")

# Estamos primero limpiando los nombres de las canciones y los nombres de los álbumes para que no tengan caracteres especiales, ni la palabra BTS, ni la frase (English Translation) y luego eliminamos los espacios en blanco al inicio y al final de cada nombre.

df['song_name'] = (
    df['song_name']
    .str.replace('BTS - ', '', regex=False)
    .str.replace('(English Translation)', '', regex=False)
    .str.replace(r'[^a-zA-ZÀ-ÿ0-9\s]', '', regex=True)
    .str.strip()
)

df['album'] = (
    df['album']
    .str.replace('BTS - ', '', regex=False)
    .str.replace('(English Translation)', '', regex=False)
    .str.strip()
)

# Aplicamos la función directamente a toda la columna
df["release_date"] = df["release_date"].apply(parsear_fecha_diccionario)

df['featured_artists'] = df['featured_artists'].replace('[]', pd.NA)

print(df.head())
print(df.count(axis=0))