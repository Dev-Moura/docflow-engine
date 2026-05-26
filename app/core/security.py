from jose import jwt
from app.core.config import Settings
from passlib.context import CryptContext
from datetime import (
    datetime,
    timedelta,
    UTC
)

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(
    plain_password: str,
    hashed_password: str
) -> bool:
    
    return pwd_context.verify(
        plain_password,
        hashed_password
    )


def create_acess_token(
        subject: str,
) -> str:
    
    expire_delta = timedelta(
        minutes=Settings.ACCES_TOKEN_EXPIRE_MINUTES
    )

    expire = datetime.now(UTC) + expire_delta

    to_encode = {
        "sub":subject,
        "exp": expire,
    }

    encoded_jwt = jwt.encode(
        to_encode,
        Settings.SECRET_KEY,
        algorithm=Settings.ALGORITHM
    )
    
    return encoded_jwt