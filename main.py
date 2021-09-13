import uvicorn
from fastapi import FastAPI
from Models.UserModel import UserModel
import MySQLdb

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.post("/login/")
async def create_item(item: UserModel):
    print(item.name)
    db = MySQLdb.connect(user="root", passwd="", host="localhost", db="gestau")
    cursor = db.cursor()
    cursor.execute("SELECT * from users")
    data = cursor.fetchall()
    for row in data:
        print(row)
    db.close()
    return data


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
