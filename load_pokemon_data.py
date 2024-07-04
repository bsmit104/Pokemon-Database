import pandas as pd
from sqlalchemy import create_engine

# Define the path to your CSV file
csv_file = 'pokemon.csv'

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(csv_file)

# Replace the type names with their corresponding IDs
type_mapping = {
    'Normal': 1,
    'Fire': 2,
    'Water': 3,
    'Electric': 4,
    'Grass': 5,
    'Ice': 6,
    'Fighting': 7,
    'Poison': 8,
    'Ground': 9,
    'Flying': 10,
    'Psychic': 11,
    'Bug': 12,
    'Rock': 13,
    'Ghost': 14,
    'Dragon': 15,
    'Dark': 16,
    'Steel': 17,
    'Fairy': 18,
}

# Map type names to type IDs
df['type1'] = df['Type 1'].map(type_mapping)
df['type2'] = df['Type 2'].map(type_mapping).fillna(0).astype(int)

# Check if the mapping was successful
print(df[['pokemonName', 'Type 1', 'type1', 'Type 2', 'type2']].head())

# Define the connection string for your PostgreSQL database
db_url = 'postgresql://postgres:Yatzsql1@localhost:5432/pokemon'

# Create a SQLAlchemy engine
engine = create_engine(db_url)

# Connect to the database 
# [['Name', 'type1', 'type2', 'Total', 'HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']]
try:
    with engine.connect() as conn:
        # Insert data into the 'Pokemon' table within the 'pokedex' schema
        #if not df.empty:
            df.to_sql(
                'allPokemon',
                con=conn,
                schema='pokedex',
                if_exists='append',
                index=False,
                method='multi',
                chunksize=100  # Use chunksize for better performance with large data
            )
            print("Data inserted successfully.")
        #else:
            #print("DataFrame is empty, no data to insert.")
except Exception as e:
    print(f"Error occurred: {str(e)}")

# Function to show data from each table
def show_table_data(table_name):
    query = f"SELECT * FROM pokedex.{table_name}"
    df = pd.read_sql(query, engine)
    print(f"\nData from {table_name} table:")
    print(df.head())

# Show data from each table after insertion
show_table_data('pokemonType')
show_table_data('allPokemon')
show_table_data('pokemonMove')

print("Data has been successfully inserted into the database.")



#####################################################################











# import pandas as pd
# from sqlalchemy import create_engine

# # Define the path to your CSV file
# csv_file = 'Pokemon.csv'

# # Read the CSV file into a pandas DataFrame
# df = pd.read_csv(csv_file)

# # Replace the type names with their corresponding IDs
# type_mapping = {
#     'Normal': 1,
#     'Fire': 2,
#     'Water': 3,
#     'Electric': 4,
#     'Grass': 5,
#     'Ice': 6,
#     'Fighting': 7,
#     'Poison': 8,
#     'Ground': 9,
#     'Flying': 10,
#     'Psychic': 11,
#     'Bug': 12,
#     'Rock': 13,
#     'Ghost': 14,
#     'Dragon': 15,
#     'Dark': 16,
#     'Steel': 17,
#     'Fairy': 18,
# }

# # Map type names to type IDs
# df['type1'] = df['Type 1'].map(type_mapping)
# df['type2'] = df['Type 2'].map(type_mapping).fillna(0).astype(int)

# # Check if the mapping was successful
# print(df[['Name', 'Type 1', 'type1', 'Type 2', 'type2']].head())

# # Define the connection string for your PostgreSQL database
# db_url = 'postgresql://postgres:Yatzsql1@localhost:5432/pokemon'

# # Create a SQLAlchemy engine
# engine = create_engine(db_url)

# # Connect to the database
# with engine.connect() as conn:
#     # Insert data into the 'Pokemon' table within the 'pokedex' schema
#     if not df.empty:
#         # print("loadin")
#         df[['Name', 'type1', 'type2', 'Total', 'HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']].to_sql(
#             'Pokemon',
#             con=conn,
#             schema='pokedex',
#             if_exists='append',
#             index=False,
#             method='multi',
#             chunksize=100  # Use chunksize for better performance with large data
#         )
#     else:
#         print("empty")

# # Function to show data from each table
# def show_table_data(table_name):
#     query = f"SELECT * FROM pokedex.{table_name}"
#     df = pd.read_sql(query, engine)
#     print(f"\nData from {table_name} table:")
#     print(df.head())

# # Show data from each table after insertion
# show_table_data('Type')
# show_table_data('Pokemon')
# show_table_data('Move')

# print("Data has been successfully inserted into the database.")

# import pandas as pd
# import psycopg2
# from sqlalchemy import create_engine

# # Define the path to your CSV file
# csv_file = 'pokemon.csv'

# # Read the CSV file into a pandas DataFrame
# df = pd.read_csv(csv_file)

# # Replace the type names with their corresponding IDs
# type_mapping = {
#     'Fire': 1,
#     'Water': 2,
#     'Grass': 3,
#     # Add all other type mappings here
# }

# df['type1'] = df['Type 1'].map(type_mapping)
# df['type2'] = df['Type 2'].map(type_mapping).fillna(0).astype(int)

# # Define the connection string for your PostgreSQL database
# db_url = 'postgresql://postgres:Yatzsql1@localhost:5432/pokemon'

# # Create a SQLAlchemy engine
# engine = create_engine(db_url)

# # Connect to the database
# with engine.connect() as conn:
#     # Insert data into the 'pokemon' table within the 'pokedex' schema
#     df[['Name', 'type1', 'type2', 'Total', 'HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']].to_sql(
#         'pokemon',
#         con=conn,
#         schema='pokedex',
#         if_exists='append',
#         index=False,
#         method='multi'
#     )

# print("Data has been successfully inserted into the database.")