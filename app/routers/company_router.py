from fastapi import APIRouter, Depends, status, Query
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
def get_companies_endpoint(skip: int = Query(0, ge=0, description="Number of records to skip for pagination"), 
                           limit: int = Query(100, ge=1, le=100, description="Maximum number of records to return"), 
                           _companyservice: CompanyService = Depends()):
    # Fetch companies from the repository layer using the DB session
    return  _companyservice.get_companies( skip=skip, limit=limit)
    