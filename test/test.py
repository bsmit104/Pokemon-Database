import pandas as pd
from sqlalchemy import create_engine

# Define the path to your CSV file
csv_file = 'example.csv'

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(csv_file)

# Define the connection string for your PostgreSQL database
db_url = 'postgresql://postgres:Yatzsql1@localhost:5432/pokemon'

# Create a SQLAlchemy engine
engine = create_engine(db_url)

# Connect to the database and insert data into the table
try:
    with engine.connect() as conn:
        # Insert data into the 'example_table' within the 'test_schema' schema
        df.to_sql(
            'example_table',
            con=conn,
            schema='test_schema',
            if_exists='append',
            index=False,
            method='multi',
            chunksize=100  # Use chunksize for better performance with large data
        )
        print("Data inserted successfully.")
except Exception as e:
    print(f"Error occurred: {str(e)}")