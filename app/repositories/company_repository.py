from fastapi import Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.company_model import Company


class CompanyRepository:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def create(self, db_company: Company):
        self.db.add(db_company)
        self.db.commit()
        self.db.refresh(db_company)

        return db_company

    def get_companies(self, skip: int = 0, limit: int = 100):
        return self.db.query(Company).offset(skip).limit(limit).all()
 