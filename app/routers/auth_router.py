from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from app.services.user_service import UserService
from app.schemas.user_schema import UserCreate, UserResponse, Token

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

@router.post("/login", response_model=Token)
def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    service: UserService = Depends()
):
    """
    OAuth2 compatible token login, getting an access token for future requests.    
    """
    return service.login(email=form_data.username, password=form_data.password)