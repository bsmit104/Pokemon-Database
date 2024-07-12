-- -- Drop the existing role if it exists
-- DROP ROLE IF EXISTS brayden;

-- -- Create the role brayden with the desired password and privileges
-- CREATE ROLE brayden LOGIN PASSWORD 'Yatzsql1' CREATEROLE;

-- -- Grant all privileges on the public schema to brayden
-- GRANT ALL PRIVILEGES ON SCHEMA public TO brayden;

-- -- Grant usage privilege on the public schema to brayden
-- GRANT USAGE ON SCHEMA public TO brayden;

-- -- Alter default privileges for future tables in the public schema
-- ALTER DEFAULT PRIVILEGES IN SCHEMA public
--     GRANT ALL ON TABLES TO brayden;
-------------------------------------------------------

DROP SCHEMA IF EXISTS pokedex CASCADE;
CREATE SCHEMA pokedex;

-- Create the Type table
CREATE TABLE pokedex.pokemonType (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);

-- -- Insert data into the Type table
-- INSERT INTO pokedex.Type (name) VALUES 
-- ('Normal'), ('Fire'), ('Water'), ('Electric'), ('Grass'), ('Ice'), ('Fighting'),
-- ('Poison'), ('Ground'), ('Flying'), ('Psychic'), ('Bug'), ('Rock'), ('Ghost'),
-- ('Dragon'), ('Dark'), ('Steel'), ('Fairy');

-- Create the Pokemon table
-- CREATE TABLE pokedex.allPokemon (
--     id SERIAL PRIMARY KEY,
--     pokemonName VARCHAR(50) NOT NULL,
--     total INTEGER,
--     hp INTEGER,
--     attack INTEGER,
--     defense INTEGER,
--     speed INTEGER
-- );
CREATE TABLE pokedex.allPokemon (
    id SERIAL PRIMARY KEY,
    rowNum INTEGER,
    pokemonName VARCHAR(50) NOT NULL,
    type1 INTEGER REFERENCES pokedex.pokemonType(id),
    type2 INTEGER REFERENCES pokedex.pokemonType(id),
    total INTEGER,
    hp INTEGER,
    attack INTEGER,
    defense INTEGER,
    sp_atk INTEGER,
    sp_def INTEGER,
    speed INTEGER
);

-- Create the Move table
CREATE TABLE pokedex.pokemonMove (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    type_id INTEGER REFERENCES pokedex.pokemonType(id),
    power INTEGER,
    accuracy INTEGER
);

-- DROP SCHEMA Pokedex CASCADE;
-- CREATE SCHEMA Poxedex;

-- -- Create the Type table
-- CREATE TABLE Type (
--     id SERIAL PRIMARY KEY,
--     name VARCHAR(50) NOT NULL
-- );

-- -- Create the Pokemon table
-- CREATE TABLE Pokemon (
--     id SERIAL PRIMARY KEY,
--     name VARCHAR(50) NOT NULL,
--     type1 INTEGER REFERENCES Type(id),
--     type2 INTEGER REFERENCES Type(id),
--     total INTEGER,
--     hp INTEGER,
--     attack INTEGER,
--     defense INTEGER,
--     sp_atk INTEGER,
--     sp_def INTEGER,
--     speed INTEGER
-- );

-- -- Create the Move table
-- CREATE TABLE Move (
--     id SERIAL PRIMARY KEY,
--     name VARCHAR(50) NOT NULL,
--     type_id INTEGER REFERENCES Type(id),
--     power INTEGER,
--     accuracy INTEGER
-- );
---------------------------------------------

-- -- Create the Pokemon table
-- CREATE TABLE Pokemon (
--     id SERIAL PRIMARY KEY,
--     name VARCHAR(50) NOT NULL,
--     type1 INTEGER REFERENCES Type(id),
--     type2 INTEGER REFERENCES Type(id),
--     hp INTEGER,
--     attack INTEGER,
--     defense INTEGER,
--     speed INTEGER,
--     generation INTEGER
-- );