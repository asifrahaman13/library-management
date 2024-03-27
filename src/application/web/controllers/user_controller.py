from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from src.internal.entities.user import UserBase
from src.infastructure.repositories.auth_repository import AuthRepository
from src.internal.use_cases.auth_service import AuthenticationService
from src.internal.interfaces.auth_interface import AuthInterface
from src.internal.use_cases.user_service import UserService
from src.internal.interfaces.user_interface import UserInterface
from src.infastructure.repositories.user_repository import UserRepository
from src.infastructure.exceptions.exceptions import HttePrequestErrors
from src.internal.helper.helper import get_current_user

# Initialize the APIRouter configuration.
router = APIRouter()

# Initialize the OAuth2PasswordBearer configuration.
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Call the AuthRepository class to create an instance of the class.
auth_repository = AuthRepository()
auth_service = AuthenticationService(auth_repository)

# Call the UserRepository class to create an instance of the class.
user_repository = UserRepository()
user_service = UserService(user_repository=user_repository)


@router.post("/signup")
async def signup(user: UserBase, user_interface: UserInterface = Depends(user_service)):
    # Convert the user data to a dictionary
    user_data = user.model_dump()
    try:
        # Call the create_user method from the user_interface to insert the data into the database.
        user_interface.create_user(user_data)
        return {"message": "User created successfully"}
    except Exception as e:
        print(e)
        return {"message": "User creation failed"}


@router.post("/login")
async def all_data(
    user: UserBase,
    auth_interface: AuthInterface = Depends(auth_service),
    user_interface: UserInterface = Depends(user_service),
):

    # Perform some assertions and checks
    assert user is not None, "User data is required"
    user_data = user.model_dump()
    assert "username" in user_data, "Username is missing"
    assert "password" in user_data, "Password is missing"

    user_data = user.model_dump()
    username = user_data["username"]
    password = user_data["password"]

    # Check if user exists
    user_exists = user_interface.check_if_user_exists(username)

    if not user_exists:
        return HttePrequestErrors.detail_not_found()

    # Check if password matches
    password_matches = user_interface.check_if_password_matches(username, password)

    if not password_matches:
        return HttePrequestErrors.unauthorized()

    try:
        # Generate an access token

        access_token = auth_interface.create_access_token(data={"sub": username})
        print(access_token)
        # Return the access token.
        return {"access_token": access_token, "token_type": "bearer"}
    # In case of an exception, return an HTTP 401 error
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )


@router.get("/authenticate")
async def get_protected_data(
    current_user: str = Depends(get_current_user),
    auth_interface: AuthInterface = Depends(auth_service),
):
    print(current_user)
    user = auth_interface.get_current_user(current_user)
    print(user)

    if user is None:
        return HttePrequestErrors.unauthorized()
    return {"message": True, "user": user}
