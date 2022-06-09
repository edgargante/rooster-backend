from pydantic import *


class UserRequestModel(BaseModel):
    id: int
    name: str
    email: str
    password: str
    role: int


class LoginRquestModel(BaseModel):
    email: str
    password: str