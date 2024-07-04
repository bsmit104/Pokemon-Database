DROP SCHEMA IF EXISTS pokedextest CASCADE;
CREATE SCHEMA pokedextest;

CREATE TABLE pokedextest.allPokeTest (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    total INTEGER,
    hp INTEGER,
    attack INTEGER,
    defense INTEGER,
    speed INTEGER
);
