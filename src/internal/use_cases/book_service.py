from src.internal.interfaces.book_interface import BookInterface
from src.infastructure.repositories.book_repositoy import BookRepository
from src.internal.entities.book import BookBase


class BookService:

    def __call__(self) -> BookInterface:
        return self

    def __init__(self, book_repository=BookRepository):
        self.book_repository = book_repository

    def get_all_books(self, user: str):
        return self.book_repository.get_all_books(user)

    def get_book_by_id(self, isbn: str, user: str):
        return self.book_repository.get_book_by_id(isbn, user)

    def create_book(self, book):
        return self.book_repository.create_book(book)

    def update_book(self, user: str, isbn, book: BookBase):
        return self.book_repository.update_book(user, isbn, book)

    def delete_book(self, user: str, isbn):
        return self.book_repository.delete_book(user, isbn)
