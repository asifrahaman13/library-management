from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Check if SQL_DB_PATH is set
assert "SQL_DB_PATH" in os.environ, "SQL_DB_PATH environment variable is not set"
assert "SECRET_KEY" in os.environ, "SECRET_KEY"

# Get the value of SQL_DB_PATH
sql_db_path = os.getenv("SQL_DB_PATH")
secret_key=os.getenv("SECRET_KEY")

# Check if the SQL_DB_PATH value is not empty
assert sql_db_path, "SQL_DB_PATH environment variable is empty"
assert secret_key, "SECRET_KEY environment variable is empty"

# Perform other checks as needed

print("All assertion checks passed. SQL_DB_PATH:", sql_db_path, secret_key)
