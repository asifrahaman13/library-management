import re
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer


# Initialize the OAuth2PasswordBearer configuration.
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_current_user(token: str = Depends(oauth2_scheme)):
    return token


def is_valid_password(password):
    # Check if the password is at least 6 characters long
    if len(password) < 8:
        return False

    # Check if the password contains at least one letter and one number
    if not re.search(r"[a-zA-Z]", password) or not re.search(r"\d", password):
        return False

    return True
