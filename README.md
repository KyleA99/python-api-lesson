# python-api-lesson

## What are we doing?
We are going to build an API endpoint that allows us to fetch data from a public, third-party API.  Essentially, we are going to create a "wrapper" that integrates to an external API so that we can easily query data from the external API.

The third-party API we are going to integrate with is open-meteo (https://api.open-meteo.com/v1/forecast
) because it is free and publicly available third-party endpoint that doesnt need an api key.

## What is an API?
An application programming interface (API) is a connection/interface between 2 computer programs.  It is an intermediary that defines and passes information between 2 the entities.

## What will we be using?
We will use Python, the FastAPI python framework, Uvicorn for the server, and an HTTP client.  FYI FastAPI seems to have a lot of abstraction, but that is part of why I chose it - it's quick to get something up and running.

## Why are we using these?
Python's simplicity and readability make it an ideal language for us to use while learning.  FastAPI is beginner-friendly and has some nice features like built in Swagger document generation and input validation.

## Actual Steps

### Install Necessary Dependencies (macOS)

Installing python:
```
brew install python
```

Installing dependencies:
```
pip3 install fastapi uvicorn requests
```

### Create main.py File
In the root directory of our project, we will create a main.py file to encapsulate our main logic.
```
my-api-tutorial/
│── main.py
```

### Dependency Imports and FastAPI Instantiation
We can start by importing our necessary dependencies into our main.py file, and instantiating a FastAPI application.

```python
from fastapi import FastAPI
import requests

app = FastAPI()
```

### Build GET Endpoint
In this code we are essentially hitting the open-meteo weather api with latitude and longitude query parameters to get the current weather.  The decorator above the function declaration defines our route.

```python
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
```

### Start Uvicorn Server
```
uvicorn main:app --reload --port 8000
```

We can now navigate to this url to view the endpoint we created: http://localhost:8000/docs

### Add Error-Handling
We can add some error handling in our get_weather() function to return a error message if something fails during the HTTP request.
```python
if response.status_code != 200:
    return {"error": "Failed to fetch weather data"}
```

### Separation of Concerns
Let's break code up into a controller layer and a service layer. The controller will handle the HTTP request and response, while the service layer will handle all of the business logic for hitting the open-meteo API.

### Add Function Headers

### Add Return Type Declaration

### What is Next?
we can build it something similar in flask