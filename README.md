# Flask To-Do List App

## About The Project
This is a simple To-do list app using Flask, SQLAlchemy, PostgreSQL, and semantic UI.

Python3.

## Getting Started

## Setup

Clone the repository and step inside.

Set up a .env file in the project directory that looks like this:
```
DATABASE_URL='postgresql+psycopg2://user:pass@localhost/todolist'
```
You'll need to create a new postgres database called 'todolist' and update the DATABASE_URL to contain your username and password.

Feel free to use a different dbms. Update the DATABASE_URL accordingly.

## How To Run

Create a virtual environment within your project directory and activate it (not required, but highly recommended)
```
python3 -m venv venv
```
```
source venv/bin/activate
```

Install required packages:
```
pip install -r requirements.txt
```

Start up the server:
```
export FLASK_APP=app.py

python -m flask run
```

Open your browser and navigate to:
```
http://127.0.0.1:5000/
```