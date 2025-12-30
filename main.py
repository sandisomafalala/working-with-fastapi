from fastapi import FastAPI
import psycopg2
from psycopg2.extras import RealDictCursor
import settings

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/users/{id}")
async def get_user(user_id: int):
    try:
        conn = psycopg2.connect(host=settings.host, database=settings.database, user=settings.user, password=settings.password)
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM users where id = {user_id}")
        row = cursor.fetchone()
        conn.close()

        return {"message": row}

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    return {"message": f"User with id {user_id} does not exist"}

@app.get("/users")
async def get_all_users():
    try:
        conn = psycopg2.connect(host=settings.host, database=settings.database, user=settings.user, password=settings.password)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        print(rows)
        conn.close()

        return {"message": rows}

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


if __name__ == "__main__":
    print('Starting server...')
    print('done')