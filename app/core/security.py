from datetime import datetime, timedelta, timezone
import bcrypt
import jwt

from app.core.config import settings

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Compares a plain text password against the database hash."""
    password_bytes = plain_password.encode('utf-8')
    hash_bytes = hashed_password.encode('utf-8')
    return bcrypt.checkpw(password_bytes, hash_bytes)

def get_password_hash(password: str) -> str:
    """Hashes a password for secure database storage using native bcrypt."""
    password_bytes = password.encode('utf-8')
    # Generate a salt and hash the password in one step
    hashed_bytes = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
    # Return as a standard string for the database
    return hashed_bytes.decode('utf-8')

def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
    to_encode = data.copy()
    
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=settings.access_token_expire_minutes)
        
    to_encode.update({"exp": expire})
    
    encoded_jwt = jwt.encode(to_encode, settings.secret_key, algorithm=settings.algorithm)
    return encoded_jwt