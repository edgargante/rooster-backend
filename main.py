from fastapi import *

import database
from database import *
from schemas import *

app = FastAPI()


@app.on_event('startup')
def startup():
    if database.is_closed():
        database.connect()


@app.on_event('shutdown')
def shutdown():
    if not database.is_closed():
        database.close()


@app.post('/user')
async def create_user(user_request: UserRequestModel):
    user = User.create(
        id=user_request.id,
        name=user_request.name,
        email=user_request.email,
        password=user_request.password,
        role=user_request.role
    )
    return user_request


@app.get('/user/{user_id}')
async def get_user(user_id):
    user = User.select().where(User.id == user_id).first()

    if user:
        return UserRequestModel(
            id=user.id,
            name=user.name,
            email=user.email,
            password=user.password,
            role=user.role
        )
    else:
        return HTTPException(404, 'User not found')


@app.get('/user/login/{user_email},{user_password}')
async def login(user_email, user_password):
    user = User.select().where(
        User.email == user_email,
        User.password == user_password
    ).first()

    if user:
        return UserRequestModel(
            id=user.id,
            name=user.name,
            email=user.email,
            password=user.password,
            role=user.role
        )
    else:

        return HTTPException(404, 'Credenciales no válidas')


@app.put('/user/{user_id}')
async def update_user(user_request: UserRequestModel):
    user = User.select().where(User.id == user_request.id).first()

    if user:
        User.update(
            {
                User.name: user_request.name
            }
        ).where(User.id == user_request.id).execute()
        return user_request

    else:
        return HTTPException(404, 'User not found')


@app.delete('/user/{user_id}')
async def delete_user(user_id):
    user = User.select().where(User.id == user_id).first()

    if user:
        user.delete_instance()
        return True
    else:
        return HTTPException(404, 'User not found')
