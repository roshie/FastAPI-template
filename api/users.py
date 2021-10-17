from fastapi import APIRouter
from main import db
from errors import Error403, Error404, Error500

users = APIRouter(
            prefix="/users",
            tags=["Users"]
            # Tags are used for categorizing APIs
        )

@users.get('')
def get_users():
    try:
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM user")
        result = cursor.fetchall()
    except Exception as e:
        print(e)
        return Error500("db-error")
        
    return {"data": result}

@users.post('')
def post_users(data: dict):
    try:
        cursor = db.cursor()
        query = f"INSERT INTO user VALUES('{data['email']}', 'password', NULL, 'Hello!')"
        cursor.execute(query)
        db.commit()
    except Exception as e:
        print(e)
        return Error500("db-error")
    return {"message": "Success"}

@users.get('/{count}')
def get_n_users(count: int):
    try:
        cursor = db.cursor(dictionary=True)
        cursor.execute(f"SELECT * FROM user LIMIT {count}")
        result = cursor.fetchall()
    except Exception as e:
        print(e)
        return Error500("db-error")
        
    return {"data": result}

@users.delete('')
def delete_users(data: dict):
    try:
        cursor = db.cursor()
        query = f"DELETE FROM user WHERE email = '{data['email']}'"
        cursor.execute(query)
        db.commit()
    except Exception as e:
        print(e)
        return Error500("db-error")

    return {"message": "Success"}