# BTS: Análisis de Música y Álbumes

### 1) Creación del dataset

Para crear el dataset se utilizará la [API de Genius](https://genius.com/api-clients). Primero, es necesario generar un **Client Access Token**.

Una vez obtenido el token, ejecutar los siguientes scripts **en orden**:

1. Ejecutar `download_songs.py` para descargar la información de las canciones.
2. Ejecutar `add_album.py` para agregar la información de los álbumes al dataset.

----

### 2) Limpieza del dataset

Para esto usaremos Pandas y haremos limpieza de nuestros datos, particularmente los nombres de las canciones serán limpiados. 

Ejecutar `clean_dataset.py` para realizar la limpieza. 

----

### 3) Iniciar el análisis
