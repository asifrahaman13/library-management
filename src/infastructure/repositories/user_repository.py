from sqlmodel import Session, SQLModel, create_engine, select
from src.internal.entities.user import  UserDatabase
from config.config import sql_db_path


class UserRepository:
    """
    Initialize the database and the configurations
    """

    def __init__(self):

        self.sqlite_url = sql_db_path
        self.engine = create_engine(self.sqlite_url)
        SQLModel.metadata.create_all(self.engine)

    # Create a user
    def create_user(self, user_data: dict):

        try:
            # Create a session
            with Session(self.engine) as session:
                # Create a user object
                user = UserDatabase(**user_data)

                # Add the user to the session
                session.add(user)

                # Commit the session
                session.commit()

                # Return the user in case it exists
                return user

        # If an error occurs, print the error
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def check_if_user_exists(self, username):
        try:
            # Create a session
            with Session(self.engine) as session:

                # Select the user from the database from the username field.
                statement = select(UserDatabase).where(
                    UserDatabase.username == username
                )

                # Execute the statement and get the first result
                results = session.exec(statement).first()

                # If the result exists, return True
                if results:
                    return True
                return False

        # If an error occurs, print the error
        except Exception as e:
            return False

    def check_if_password_matches(self, username, password):
        try:
            # Create a session
            with Session(self.engine) as session:
                # Select the user from the database from the username field.
                statement = select(UserDatabase).where(
                    UserDatabase.username == username
                )

                # Execute the statement and get the first result
                results = session.exec(statement).first()
                if results:
                    # If the password matches the password in the database, return True
                    if results.password == password:
                        return True
                return False
        except Exception as e:
            return False
