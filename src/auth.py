import os
import bcrypt
import jwt

from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")


# Example hashed password for "password123"
STORED_PASSWORD = bcrypt.hashpw(
    b"password123",
    bcrypt.gensalt()
)


def authenticate(username, password):
    if username != "admin":
        return None

    if not bcrypt.checkpw(
        password.encode(),
        STORED_PASSWORD
    ):
        return None

    token = jwt.encode(
        {"username": username},
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return token
