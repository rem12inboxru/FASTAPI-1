from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
async def welcome() -> dict:
    return {"message": f"Главная страница"}


@app.get("/user/admin")
async def admin() -> dict:
    return {"message": f"Вы вошли как администратор"}

@app.get("/user/{name}/{age}")
async def name_age(name: str, age: int) -> dict:
    return {"message": f"Информация о пользователе. Имя {name}. Возраст {age} "}


@app.get("/user/{user_id}")
async def user_id_in(user_id: int) -> dict:
    return {"message": f"Вы вошли как пользователь № {user_id}"}




if __name__ == '__main__':
    uvicorn.run(app="main:app", reload=True)
