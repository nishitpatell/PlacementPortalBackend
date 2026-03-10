from pydantic import BaseModel

class RegisterCompanySchema(BaseModel):
    name: str
    email: str