from fastapi import Depends

from app.models.company_model import Company
from app.schemas.company_schema import CompanyCreate
from app.repositories.company_repository import CompanyRepository


class CompanyService:
    def __init__(self, repository: CompanyRepository = Depends()):
        self.repository = repository

    def create_company(self, company_data: CompanyCreate):
        db_company = Company(**company_data.model_dump())
        return self.repository.create(db_company=db_company)

    def get_companies(self, skip: int = 0, limit: int = 100):
        return self.repository.get_companies(skip=skip, limit=limit)