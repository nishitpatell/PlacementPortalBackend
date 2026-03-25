from fastapi import Depends, HTTPException, status

from app.repositories.user_repository import UserRepository
from app.models.user_model import User
from app.schemas.user_schema import UserCreate
from app.core.security import get_password_hash, verify_password, create_access_token

class UserService:
    def __init__(self, repository: UserRepository = Depends()):
        self.repository = repository

    def register_user(self, user_in: UserCreate):
        existing_user = self.repository.get_by_email(email=user_in.email)

        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="A user with this email already exists."
            )

        # 2. Security Phase: Hash the plain-text password
        hashed_pw = get_password_hash(user_in.password)
        db_user = User(
            email=user_in.email,
            hashed_password=hashed_pw,
            role=user_in.role
        )

        return self.repository.create(db_user=db_user)
    
    def authenticate_user(self, email: str, plain_password: str):
        user = self.repository.get_by_email(email=email)

        if not user or not verify_password(plain_password, user.hashed_password):
            return None
        
        return user
    
    def login(self, email: str, password: str):
        user = self.authenticate_user(email=email, plain_password=password)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password.",
                headers={"WWW-Authenticate": "Bearer"},
            )
        
        token_payload = {"sub": user.email, "role": user.role}
        access_token = create_access_token(data=token_payload)
        
        return {
            "access_token": access_token, 
            "token_type": "bearer"
        }   
        

