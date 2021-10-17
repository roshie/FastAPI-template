from fastapi import FastAPI
import mysql.connector

# MySQL Connection
db = mysql.connector.connect(
  host="",
  user="",
  password="",
  database=""
)

# Start our app
app = FastAPI()

# import routers
from api.users import users
app.include_router(users)

# Our first route
@app.get('/', tags=["Home"])
def Home():
    return {"message": "Server is running"}
