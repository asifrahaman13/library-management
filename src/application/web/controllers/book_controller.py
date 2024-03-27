from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.security import OAuth2PasswordBearer
from src.infastructure.repositories.book_repositoy import BookRepository
from src.internal.use_cases.book_service import BookService
from src.internal.interfaces.book_interface import BookInterface
from src.internal.entities.book import BookBase
from src.internal.helper.helper import get_current_user
from src.internal.interfaces.auth_interface import AuthInterface
from src.infastructure.repositories.auth_repository import AuthRepository
from src.internal.use_cases.auth_service import AuthenticationService
from src.infastructure.exceptions.exceptions import HttpRequestErrors

book_router = APIRouter()

# Call the AuthRepository class to create an instance of the class.
auth_repository = AuthRepository()
auth_service = AuthenticationService(auth_repository)

# Call the BookRepository class to create an instance of the class.
book_repository = BookRepository()
book_service = BookService(book_repository=book_repository)

# Initialize the OAuth2PasswordBearer configuration.
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@book_router.get("/books")
def get_all_books(
    current_user: str = Depends(get_current_user),
    book_interface: BookInterface = Depends(book_service),
    auth_interface: AuthInterface = Depends(auth_service),
):
    user = auth_interface.get_current_user(current_user)

    # Check if user is None
    if user is None:
        raise HTTPException(status_code=401, detail="Unauthorized")

    # Call the interface function to get all books
    all_books = book_interface.get_all_books(user)

    # Check if the all_books is not None. If yes return the all_books.
    if all_books is not None:
        json_compatible_item_data = jsonable_encoder(all_books)
        return JSONResponse(content=json_compatible_item_data)


@book_router.get("/books/{isbn}")
def get_book_by_id(
    isbn: str,
    current_user: str = Depends(get_current_user),
    auth_interface: AuthInterface = Depends(auth_service),
    book_interface: BookInterface = Depends(book_service),
):
    user = auth_interface.get_current_user(current_user)

    # Check if user is None
    if user is None:
        raise HTTPException(status_code=401, detail="Unauthorized")

    book = book_interface.get_book_by_id(isbn, user)

    # Check if the book is not None. If yes return the book.
    if book is not None:
        json_compatible_item_data = jsonable_encoder(book)
        return JSONResponse(content=json_compatible_item_data)


@book_router.post("/books")
def create_book(
    book: BookBase,
    book_interface: BookInterface = Depends(book_service),
    current_user: str = Depends(get_current_user),
    auth_interface: AuthInterface = Depends(auth_service),
):
    user = auth_interface.get_current_user(current_user)

    # Check if user is None
    if user is None:
        raise HTTPException(status_code=401, detail="Unauthorized")

    # Set the user from the token to the book object
    book.User = user
    book_cretaed = book_interface.create_book(book)

    # Check if the book is created. If yes return the book.
    if book_cretaed is not None:
        json_compatible_item_data = jsonable_encoder(book_cretaed)
        return JSONResponse(content=json_compatible_item_data)

    return HttpRequestErrors.not_valid()


@book_router.put("/books/{isbn}")
def update_book(
    isbn: str,
    book: BookBase,
    book_interface: BookInterface = Depends(book_service),
    current_user: str = Depends(get_current_user),
    auth_interface: AuthInterface = Depends(auth_service),
):
    user = auth_interface.get_current_user(current_user)

    if user is None:
        raise HTTPException(status_code=401, detail="Unauthorized")

    # Call the interface function to update the book
    response = book_interface.update_book(user, isbn, book)

    # Check if the response is not None. Otherwise return the response.
    if response is not None:
        json_compatible_item_data = jsonable_encoder(response)
        return JSONResponse(content=json_compatible_item_data)


@book_router.delete("/books/{isbn}")
def delete_book(
    isbn: str,
    book_interface: BookInterface = Depends(book_service),
    current_user: str = Depends(get_current_user),
    auth_interface: AuthInterface = Depends(auth_service),
):
    user = auth_interface.get_current_user(current_user)

    # Check if user is None
    if user is None:
        raise HTTPException(status_code=401, detail="Unauthorized")

    # Call the interface function to delete the book
    deleted_book = book_interface.delete_book(user, isbn)

    # Check if the book is deleted. If yes return the deleted book.
    if deleted_book is not None:
        json_compatible_item_data = jsonable_encoder(deleted_book)
        return JSONResponse(content=json_compatible_item_data)
