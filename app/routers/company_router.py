from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.repositories import company_repository
from app.schemas.company_schema import CompanyResponse, CompanyCreate
from app.services.company_service import CompanyService


router = APIRouter(
    prefix="/companies",
    tags=["companies"]
)

@router.post("", response_model=CompanyResponse, status_code=status.HTTP_201_CREATED)
def create_company_endpoint(company_in: CompanyCreate, _companyservice: CompanyService = Depends()):
    # Hand off the validated data and the DB session to the repository layer
    return _companyservice.create_company(company_data=company_in)

@router.get("", response_model=list[CompanyResponse])
def get_companies_endpoint(skip: int = 0, limit: int = 100, _companyservice: CompanyService = Depends()):
    # Fetch companies from the repository layer using the DB session
    return  _companyservice.get_companies( skip=skip, limit=limit)
    