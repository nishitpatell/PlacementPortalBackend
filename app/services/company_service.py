from fastapi import Depends
from sqlalchemy.orm import Session

from app.schemas.company_schema import CompanyCreate
from app.repositories.company_repository import CompanyRepository


class CompanyService:
    def __init__(self, repository: CompanyRepository = Depends()):
        self.repository = repository

    def create_company(self, company_data: CompanyCreate):
        return self.repository.create(company_data=company_data)
    
    def get_companies(self, skip: int = 0, limit: int = 100):
        return self.repository.get_companies(skip=skip, limit=limit)