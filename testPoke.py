import pandas as pd
from sqlalchemy import create_engine

# Define the path to your CSV file
csv_file = 'pokemon.csv'

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
    
    
# import pandas as pd
# from sqlalchemy import create_engine

# # Define the path to your CSV file
# csv_file = 'poke.csv'

# # Read the CSV file into a pandas DataFrame
# df = pd.read_csv(csv_file)

# # Define the connection string for your PostgreSQL database
# db_url = 'postgresql://postgres:Yatzsql1@localhost:5432/pokemon'

# # Create a SQLAlchemy engine
# engine = create_engine(db_url)

# # Connect to the database and insert data into the table
# try:
#     with engine.connect() as conn:
#         # Insert data into the 'example_table' within the 'test_schema' schema
#         df.to_sql(
#             'allPokeTest',
#             con=conn,
#             schema='pokedextest',
#             if_exists='append',
#             index=False,
#             method='multi',
#             chunksize=100  # Use chunksize for better performance with large data
#         )
#         print("Data inserted successfully.")
# except Exception as e:
#     print(f"Error occurred: {str(e)}")

# import pandas as pd
# from sqlalchemy import create_engine, text

# # Define the connection string for your PostgreSQL database
# db_url = 'postgresql://postgres:Yatzsql1@localhost:5432/pokemon'

# # Create a SQLAlchemy engine
# engine = create_engine(db_url)

# # Read and execute the SQL script for schema and table creation
# def execute_sql_script(engine, script_path):
#     with open(script_path, 'r') as file:
#         sql_script = file.read()
#     with engine.connect() as conn:
#         conn.execute(text(sql_script))

# # Execute the schema and table creation script
# execute_sql_script(engine, 'testPokeSchema.sql')

# # Function to check if the schema exists
# def check_schema_exists(engine, schema_name):
#     query = text(f"SELECT schema_name FROM information_schema.schemata WHERE schema_name = :schema_name")
#     with engine.connect() as conn:
#         result = conn.execute(query, {"schema_name": schema_name}).fetchone()
#     return result is not None

# # Function to check if the table exists
# def check_table_exists(engine, schema_name, table_name):
#     query = text(f"SELECT table_name FROM information_schema.tables WHERE table_schema = :schema_name AND table_name = :table_name")
#     with engine.connect() as conn:
#         result = conn.execute(query, {"schema_name": schema_name, "table_name": table_name}).fetchone()
#     return result is not None

# # Function to get the table structure
# def get_table_structure(engine, schema_name, table_name):
#     query = text(f"SELECT column_name, data_type FROM information_schema.columns WHERE table_schema = :schema_name AND table_name = :table_name")
#     with engine.connect() as conn:
#         result = conn.execute(query, {"schema_name": schema_name, "table_name": table_name}).fetchall()
#     return result

# # Check if the schema exists
# if check_schema_exists(engine, 'pokedextest'):
#     print("Schema 'pokedextest' exists.")
# else:
#     print("Schema 'pokedextest' does not exist.")

# # Check if the table exists
# if check_table_exists(engine, 'pokedextest', 'allPokeTest'):
#     print("Table 'allPokeTest' exists in schema 'pokedextest'.")
    
#     # Get the table structure
#     structure = get_table_structure(engine, 'pokedextest', 'allPokeTest')
#     print("Table structure:")
#     for column in structure:
#         print(f"Column: {column['column_name']}, Data Type: {column['data_type']}")
# else:
#     print("Table 'allPokeTest' does not exist in schema 'pokedextest'.")
    