from datetime import datetime, timedelta, timezone
from jose import JWTError, jwt
from config.config import secret_key


class AuthRepository:

    def __init__(self):
        self.secret_key = secret_key
        self.expires_delta = timedelta(minutes=3600)

    # Function to create access token
    def create_access_token(self, data: dict) -> str:
        # Take a copy of the data so that it is not manipulated.
        to_encode = data.copy()

        # Set the expiration time of the token
        expire = datetime.now(timezone.utc) + self.expires_delta

        # Add the expiration time to the data
        to_encode.update({"exp": expire})

        # Encode the data
        encoded_jwt = jwt.encode(to_encode, self.secret_key, algorithm="HS256")

        return encoded_jwt

    def get_current_user(self, token) -> str:

        try:
            # Decode the token
            payload = jwt.decode(token, self.secret_key, algorithms=["HS256"])
            # Get the username from the token
            username: str = payload.get("sub")
            if username is None:
                return None

        except JWTError:
            return None

        return username
