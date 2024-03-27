from abc import ABC, abstractmethod
from src.internal.entities.book import BookBase


class BookInterface(ABC):
    @abstractmethod
    def create_book(self, book_data: dict):
        pass

    @abstractmethod
    def get_book(self, isbn: int):
        pass

    @abstractmethod
    def get_book_by_id(self, isbn: str, user: str):
        pass

    @abstractmethod
    def get_all_books(self, user: str):
        pass

    @abstractmethod
    def update_book(self, user: str, isbn: int, book_data: BookBase):
        pass

    @abstractmethod
    def delete_book(self, user: str, isbn: int):
        pass
