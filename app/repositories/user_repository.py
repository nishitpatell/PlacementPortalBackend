from fastapi import Depends
from sqlalchemy.orm import Session

from app.models.user_model import User
from app.core.database import get_db

class UserRepository:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def create(self, db_user: User):
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user
    
    def get_by_email(self, email: str):
        return self.db.query(User).filter(User.email == email).first()