DROP SCHEMA IF EXISTS test_schema CASCADE;
CREATE SCHEMA test_schema;

CREATE TABLE test_schema.example_table (
    id SERIAL PRIMARY KEY,
    rownum INTEGER,
    pokemonname VARCHAR(50),
    type1 VARCHAR(50),
    type2 VARCHAR(50),
    total INTEGER,
    hp INTEGER,
    attack INTEGER,
    defense INTEGER,
    specialatk INTEGER,
    specialdef INTEGER,
    speed INTEGER,
    generation INTEGER,
    legendary BOOLEAN
);

CREATE TABLE test_schema.simplifiedPokemonStats (
    id SERIAL PRIMARY KEY,
    pokemonname VARCHAR(50),
    attack INTEGER,
    defense INTEGER,
    speed INTEGER
);


-- DROP SCHEMA IF EXISTS pokedextest CASCADE;
-- CREATE SCHEMA pokedextest;

-- CREATE TABLE pokedextest.allPokeTest (
--     id SERIAL PRIMARY KEY,
--     name VARCHAR(50),
--     total INTEGER,
--     hp INTEGER,
--     attack INTEGER,
--     defense INTEGER,
--     speed INTEGER
-- );


-- CREATE TABLE test_schema.example_table (
--     id SERIAL PRIMARY KEY,
--     name VARCHAR(50),
--     total INTEGER,
--     hp INTEGER,
--     attack INTEGER,
--     defense INTEGER,
--     speed INTEGER
-- );