import psycopg2
from fastapi import FastAPI, Form

import settings

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/login")
async def login(username: str, password: str):
    try:
        conn = psycopg2.connect(host=settings.host, database=settings.database, user=settings.user, password=settings.password)
        cur = conn.cursor()
        cur.execute("""SELECT * FROM creds WHERE username = %s""", username)
        creds = cur.fetchone()
        conn.close()

        if creds[2] == password:
            return {"message": "API Key"}
        else:
            return {"message": "Login Failed! Username or password incorrect"}
    except psycopg2.OperationalError as error:
        print(error)


@app.post("/signup")

@app.get("/users/{id}")
async def get_user(user_id: int):
    try:
        conn = psycopg2.connect(host=settings.host, database=settings.database, user=settings.user,
                                password=settings.password)
        cursor = conn.cursor()
        cursor.execute("""SELECT * FROM users WHERE id = %s""", str(user_id))
        row = cursor.fetchone()
        conn.close()

        return {"user": row}

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

        return {"users": rows}

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


if __name__ == "__main__":
    # TODO
    # Always commit your DB inserts and updates
    print('Starting server...')
    # conn = psycopg2.connect(host=settings.host, database=settings.database, user=settings.user, password=settings.password)
    # cursor = conn.cursor()
    # cursor.execute("""SELECT * FROM creds WHERE username = 'jane.doe'""")
    # row = cursor.fetchone()
    # conn.close()
    # print(row[2])
    print('done')
