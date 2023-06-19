import requests
from bs4 import BeautifulSoup

# URL de la página a raspar
url = "https://www.example.com"

# Realizar la solicitud HTTP GET a la página
response = requests.get(url)

# Verificar si la solicitud fue exitosa (código de estado 200)
if response.status_code == 200:
    # Crear el objeto BeautifulSoup a partir del contenido HTML de la página
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extraer la información deseada de la página
    # Aquí se muestra un ejemplo de cómo obtener todos los enlaces de la página
    enlaces = soup.find_all('a')
    
    # Imprimir los enlaces encontrados
    for enlace in enlaces:
        print(enlace['href'])
else:
    print("Error al realizar la solicitud HTTP:", response.status_code)
