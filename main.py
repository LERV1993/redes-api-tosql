import requests
import baseDeDatos

url = 'https://www.freetogame.com/api/games'
response = requests.get(url)

if response.status_code == 200: 
    data = response.json()  
    baseDeDatos.registrarDatos(data)

else: 
    print("Error:", response.status_code)