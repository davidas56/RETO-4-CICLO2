import requests

# Configura tu API key de TMDb
API_KEY = "a614f104552b03f1665eba5a038abcaa"

def obtener_rating_pelicula(pelicula):
    # Realiza una solicitud para buscar la película en TMDb
    url_busqueda = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={pelicula}"
    respuesta_busqueda = requests.get(url_busqueda)
    datos_busqueda = respuesta_busqueda.json()

    # Verifica si se encontraron resultados de búsqueda
    if datos_busqueda["results"]:
        # Obtén el ID de la primera película encontrada
        id_pelicula = datos_busqueda["results"][0]["id"]

        # Realiza una solicitud para obtener los detalles de la película
        url_detalles = f"https://api.themoviedb.org/3/movie/{id_pelicula}?api_key={API_KEY}"
        respuesta_detalles = requests.get(url_detalles)
        datos_detalles = respuesta_detalles.json()

        # Verifica si se encontraron detalles de la película
        if datos_detalles:
            rating = datos_detalles["vote_average"]
            return rating
        else:
            return "No se encontraron detalles de la película."
    else:
        return "No se encontraron resultados de búsqueda para la película."

# Prueba de la función
pelicula = input("Ingrese el título de la película: ")
rating = obtener_rating_pelicula(pelicula)
print("Rating de la película:", rating)
