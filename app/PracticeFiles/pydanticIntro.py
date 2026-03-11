# pydantic is library to perform data validation

from datetime import datetime
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    signup_ts: datetime | None = None
    friends: list[int] = []


#below ones will give error
# external_data = {
#     "signup_ts": "2017-06-01 12:22",
#     "friends": [1, "2", b"3"],
#     "name": "John Doe"
# }
# external_data = {
#     "id": "123",
#     "signup_ts": "2017-06-01 12:22",
#     "friends": [1, "2", b"3"],
#     "mane": "John Doe"
# }
# external_data = {
#     "id": "xcv",
#     "signup_ts": "2017-06-01 12:22",
#     "friends": [1, "2", b"3"],
#     "name": "John Doe"
# }

external_data = {
    "id": "123",
    "signup_ts": "2017-06-01 12:22",
    "friends": [1, "2", b"3"],
    "name": "John Doe"
}
user = User(**external_data)
print(user)
# > User id=123 name='John Doe' signup_ts=datetime.datetime(2017, 6, 1, 12, 22) friends=[1, 2, 3]
print(user.name)
# > 123

from typing import Annotated

#The important thing to remember is that the first type parameter you pass to Annotated is the actual type. The rest, is just metadata for other tools.
def say_hello(name: Annotated[str, "this is just metadata"]) -> str:
    return f"Hello {name}"