from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/weather")
def get_weather(lat: float, long: float):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={long}&current_weather=true"
    response = requests.get(url)

    data = response.json()
    current = data.get("current_weather", {})

    response_object = {
        "latitude": lat,
        "longitude": long,
        "temperature_celsius": current.get("temperature"),
        "windspeed": current.get("windspeed"),
        "weathercode": current.get("weathercode")
    }

    return response_object
