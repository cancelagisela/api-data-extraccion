import json
import requests

API_URL = "https://jsonplaceholder.typicode.com/users"

try:
    response = requests.get(API_URL, timeout=10)
    response.raise_for_status()

    users = response.json()

    clean_data = []

    for user in users:
        clean_data.append({
            "id": user["id"],
            "name": user["name"],
            "email": user["email"],
            "city": user["address"]["city"]
        })

    with open("data_extracted.json", "w", encoding="utf-8") as file:
        json.dump(clean_data, file, indent=4)

    print("Datos guardados correctamente.")

except requests.exceptions.HTTPError as e:
    print(f"Error HTTP: {e}")

except requests.exceptions.ConnectionError:
    print("Error de conexión.")

except requests.exceptions.Timeout:
    print("Tiempo agotado.")

except Exception as e:
    print(f"Error inesperado: {e}")
