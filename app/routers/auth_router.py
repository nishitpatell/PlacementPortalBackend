from fastapi import APIRouter, Depends, status
from app.services.user_service import UserService
from app.schemas.user_schema import UserCreate, UserResponse

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def register_user_endpoint(
    user_in: UserCreate, 
    _userservice: UserService = Depends()
):
    """
    Register a new user in the system.
    """

    return _userservice.register_user(user_in=user_in)