from src.internal.interfaces.user_interface import UserInterface
from src.infastructure.repositories.user_repository import UserRepository


class UserService:
    def __call__(self) -> UserInterface:
        return self

    def __init__(self, user_repository=UserRepository):
        self.user_repository = user_repository

    def create_user(self, user_data: dict):
        return self.user_repository.create_user(user_data)

    def check_if_user_exists(self, username):
        return self.user_repository.check_if_user_exists(username)

    def check_if_password_matches(self, username, password):
        return self.user_repository.check_if_password_matches(username, password)
