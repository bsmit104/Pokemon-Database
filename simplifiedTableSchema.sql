DROP SCHEMA IF EXISTS test_schema CASCADE;
CREATE SCHEMA test_schema;

CREATE TABLE test_schema.selected_columns_table (
    id SERIAL PRIMARY KEY,
    pokemonname VARCHAR(50),
    attack INTEGER,
    defense INTEGER,
    speed INTEGER
);