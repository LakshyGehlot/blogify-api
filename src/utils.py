from passlib.context import CryptContext
import jwt
from datetime import datetime, timedelta
from src.config import settings

passwordContext = CryptContext(schemes=["bcrypt"])

def hash_password(password: str) -> str:
    return passwordContext.hash(password)

def verify_password(password: str, hashed_password: str) -> bool:
    return passwordContext.verify(password, hashed_password, scheme="bcrypt")


def genrate_token(user_data: dict, refresh = False, expiry: int = 60) -> str:
    payload = {
        "user": user_data,
        "jti": user_data['uid'],
        "refresh": refresh,
        "exp": datetime.now() + timedelta(minutes=expiry)
    }
    token = jwt.encode(payload, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)
    return token

def decode_token(token: str):
    try:
        token_data = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
        return token_data
    except jwt.PyJWTError as e:
        return None