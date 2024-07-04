import pandas as pd
from sqlalchemy import create_engine, text

# Define the connection string for your PostgreSQL database
db_url = 'postgresql://postgres:Yatzsql1@localhost:5432/pokemon'

# Create a SQLAlchemy engine
engine = create_engine(db_url)

# Read and execute the SQL script for schema and table creation
def execute_sql_script(engine, script_path):
    with open(script_path, 'r') as file:
        sql_script = file.read()
    with engine.connect() as conn:
        conn.execute(text(sql_script))

# Execute the schema and table creation script
execute_sql_script(engine, 'test_Schema.sql')

# Function to check if the schema exists
def check_schema_exists(engine, schema_name):
    query = text(f"SELECT schema_name FROM information_schema.schemata WHERE schema_name = :schema_name")
    with engine.connect() as conn:
        result = conn.execute(query, {"schema_name": schema_name}).fetchone()
    return result is not None

# Function to check if the table exists
def check_table_exists(engine, schema_name, table_name):
    query = text(f"SELECT table_name FROM information_schema.tables WHERE table_schema = :schema_name AND table_name = :table_name")
    with engine.connect() as conn:
        result = conn.execute(query, {"schema_name": schema_name, "table_name": table_name}).fetchone()
    return result is not None

# Function to get the table structure
def get_table_structure(engine, schema_name, table_name):
    query = text(f"SELECT column_name, data_type FROM information_schema.columns WHERE table_schema = :schema_name AND table_name = :table_name")
    with engine.connect() as conn:
        result = conn.execute(query, {"schema_name": schema_name, "table_name": table_name}).fetchall()
    return result

# Check if the schema exists
if check_schema_exists(engine, 'test_schema'):
    print("Schema 'test_schema' exists.")
else:
    print("Schema 'test_schema' does not exist.")

# Check if the table exists
if check_table_exists(engine, 'test_schema', 'example_table'):
    print("Table 'example_table' exists in schema 'pokedextest'.")
    
    # Get the table structure
    structure = get_table_structure(engine, 'test_schema', 'example_table')
    print("Table structure:")
    for column in structure:
        print(f"Column: {column['column_name']}, Data Type: {column['data_type']}")
else:
    print("Table 'example_table' does not exist in schema 'test_schema'.")
    