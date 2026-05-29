from passlib.context import CryptContext
from jose import jwt
from datetime import timedelta, datetime, timezone
from app.core.config import settings

pwd_context = CryptContext(schemes= ["bcrypt"], deprecated= "auto")

def hash_password(password: str):
    pwd = pwd_context.hash(password)
    return pwd

def verify_password(test_password: str, hashed_password: str):
    pwd_verified = pwd_context.verify(test_password, hashed_password)
    return pwd_verified

def create_access_token(username: str):
    encode = {'sub': username}
    expires = datetime.now(timezone.utc) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    encode.update({'exp': expires})
    return jwt.encode(encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)