from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

# Define the connection string for your PostgreSQL database
db_url = 'postgresql://postgres:Yatzsql1@localhost:5432/pokemon'

try:
    # Create a SQLAlchemy engine
    engine = create_engine(db_url)

    # Test the connection by connecting to the engine
    with engine.connect() as conn:
        conn.execute(text("SELECT 1"))  # Execute a simple query to test connection
        print("Connection successful")

except SQLAlchemyError as e:
    print("Connection failed:", e)