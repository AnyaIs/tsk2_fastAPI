from pydantic import BaseModel, Field
from typing import Union, Annotated


class Main_Users(BaseModel):
    name: Union[str, None] = None
    id: Annotated[Union[int, None], Field(default =100, ge=1, lt=200)] = None


class Main_UsersDB(Main_Users):
    password: Annotated[Union[str, None], Field(max_length = 200, min_length=8)] = None

class New_Response(BaseModel):
    message: str