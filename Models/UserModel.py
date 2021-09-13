
from pydantic import BaseModel


class UserModel(BaseModel):
    name: str
    phone: str
    address: str
    param1: str

