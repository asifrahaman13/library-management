from abc import ABC, abstractmethod


class UserInterface(ABC):

    @abstractmethod
    def create_user(self, user_data: dict):
        pass

    @abstractmethod
    def check_if_user_exists(self, username)->bool:
        pass

    @abstractmethod
    def check_if_password_matches(self, username, password)->bool:
        pass