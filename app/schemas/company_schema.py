from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID

class CompanyBase(BaseModel):
    name: str
    description: str
    domains: List[str]
    website: Optional[str] = None
    hr_email: Optional[str] = None

class CompanyCreate(CompanyBase):
    pass

class CompanyResponse(CompanyBase):
    id: UUID

    # This config is strictly required for SQLAlchemy integration
    class Config:
        from_attributes = True

