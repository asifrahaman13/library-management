from sqlmodel import Session, SQLModel, create_engine, select
from src.internal.entities.book import BookDatabase
from config.config import sql_db_path


class BookRepository:
    """
    Initialize the database and the configurations
    """

    def __init__(self):

        self.sqlite_url = sql_db_path
        self.engine = create_engine(self.sqlite_url)
        SQLModel.metadata.create_all(self.engine)

    def get_all_books(self, user):
        with Session(self.engine) as session:

            # Select all the books from the database
            statement = select(BookDatabase).where(BookDatabase.User == user)

            # Execute the statement and get all the books
            books = session.exec(statement)

            # Create a list of all the books
            list_of_all_books = []

            # Loop through the books and print them
            for book in books:

                list_of_all_books.append(book)
            # Return the list of all books
            return list_of_all_books

    def get_book_by_id(self, isbn, user):
        with Session(self.engine) as session:
            # Select the book from the database from the isbn field.
            statement = select(BookDatabase).where(BookDatabase.ISBN == isbn)
            book = session.exec(statement).first()

            if user != book.User:
                return None

            # If the book exists, return the book
            return book

    def create_book(self, book):

        with Session(self.engine) as session:
            # Create a book object
            book_object = BookDatabase(**book.dict())

            # Add the book to the session
            session.add(book_object)

            # Commit the session
            session.commit()
            return book

    def update_book(self, user, isbn, book):
        try:
            book = book.dict()
            with Session(self.engine) as session:

                # Select the book from the database from the isbn field.
                statement = select(BookDatabase).where(BookDatabase.ISBN == isbn)

                # Execute the statement and get the first result
                previous_book_details = session.exec(statement).first()

                # Check if the user is the same as the previous user
                if user != previous_book_details.User:
                    return None

                # Update the book details
                previous_book_details.Title = book["Title"]
                previous_book_details.Authors = book["Authors"]
                previous_book_details.Publication_Date = book["Publication_Date"]
                previous_book_details.ISBN = book["ISBN"]
                previous_book_details.Description = book["Description"]
                previous_book_details.User = user

                # Add the book to the session
                session.add(previous_book_details)

                # Commit the session
                session.commit()

                # Refresh the session
                session.refresh(previous_book_details)
                return previous_book_details
        except Exception as e:
            return None

    def delete_book(self, user, isbn):
        try:
            with Session(self.engine) as session:
                # Select the book from the database from the isbn field.
                statement = select(BookDatabase).where(BookDatabase.ISBN == isbn)

                # Execute the statement and get the first result
                book = session.exec(statement).first()

                if user != book.User:
                    return None

                # Delete the book
                session.delete(book)

                # Commit the session
                session.commit()
                return book
        except Exception as e:
            return None
