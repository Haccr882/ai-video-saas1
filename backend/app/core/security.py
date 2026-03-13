from datetime import datetime, timedelta
from jose import jwt
from passlib.context import CryptContext

from app.core.config import settings

pwd_context = CryptContext(schemes=["bcrypt"])

ALGORITHM = "HS256"


def hash_password(password: str):
    return pwd_context.hash(password)


def verify_password(password: str, hashed: str):
    return pwd_context.verify(password, hashed)


def create_access_token(data: dict):

    expire = datetime.utcnow() + timedelta(hours=12)

    data.update({"exp": expire})

    token = jwt.encode(data, settings.JWT_SECRET, algorithm=ALGORITHM)

    return token
