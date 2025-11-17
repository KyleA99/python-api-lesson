# python-api-lesson

## What are we doing?
We are going to build an API endpoint that allows us to fetch data from a public, third-party API.  Essentially, we are going to create a "wrapper" that integrates to an external API so that we can easily query data from the external API.

## What is an API?
An application programming interface (API) is a connection/interface between 2 computer programs.  It is an intermediary that defines and passes information between 2 the entities.

## What will we be using?
We will use Python, the FastAPI python framework, Uvicorn for the server, an HTTP client, and python-dotenv for managing our environment variables (if we even have any).

## Why are we using these?
Python's simplicity and readability make it an ideal language for us to use while learning.  FastAPI is beginner-friendly and has some nice features like built in Swagger document generation and input validation.

## Actual Steps

### Install necessary dependencies (macOS)

Installing python:
```python
brew install python
```

Installing dependencies:
```python
pip3 install fastapi uvicorn requests python-dotenv
```

### Create a main.py file
In the root directory of our project, we will create a main.py file to encapsulate our main logic.
```
my-api-tutorial/
│── main.py
│── .env
```
