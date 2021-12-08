from datetime import datetime, timedelta
import time
from typing import Dict, Optional
import jwt
from decouple import config

# to get a string like this run:
# openssl rand -hex 32
SECRET_KEY = config("secret")
ALGORITHM = config("algorithm")


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    print(expires_delta)
    print(datetime.utcnow())
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
        # expire = expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    print(expire)
    print(to_encode)
    to_encode.update({"exp": expire})
    print(to_encode)
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    print(encoded_jwt)
    return encoded_jwt


# def signJWT(user_id: str) -> Dict[str, str]:
#     print(time.time())
#     payload = {
#         "userId": user_id,
#         "expires": time.time() + 600
#     }
#     token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

#     return token_response(token, user_id)


def decodeJWT(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return decoded_token if decoded_token["exp"] >= time.time() else None
    except:
        return {}
