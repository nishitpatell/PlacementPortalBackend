from fastapi import Depends, HTTPException, status

from app.repositories.user_repository import UserRepository
from app.models.user_model import User
from app.schemas.user_schema import UserCreate
from app.core.security import get_password_hash

class UserService:
    def __init__(self, repository: UserRepository = Depends()):
        self.repository = repository

    def register_user(self, user_in: UserCreate):
        print("--- CRITICAlllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllL DEBUG ---")
        existing_user = self.repository.get_by_email(email=user_in.email)

        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="A user with this email already exists."
            )
        print("--- CRITICAL DEBUG ---")
        print(f"Value: {user_in.password}")
        print(f"Type: {type(user_in.password)}")
        print(f"Length: {len(str(user_in.password))}")
        print("----------------------")

        # 2. Security Phase: Hash the plain-text password
        hashed_pw = get_password_hash(user_in.password)
        db_user = User(
            email=user_in.email,
            hashed_password=hashed_pw,
            role=user_in.role
        )

        return self.repository.create(db_user=db_user)
