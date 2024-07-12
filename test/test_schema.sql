DROP SCHEMA IF EXISTS test_schema CASCADE;
CREATE SCHEMA test_schema;

CREATE TABLE test_schema.example_table (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    total INTEGER,
    hp INTEGER,
    attack INTEGER,
    defense INTEGER,
    speed INTEGER
);

-- CREATE TABLE test_schema.example_table (
--     id SERIAL PRIMARY KEY,
--     name VARCHAR(50),
--     age INTEGER,
--     city VARCHAR(50)
-- );

-- name,age,city
-- Alice,30,New York
-- Bob,25,Los Angeles
-- Charlie,35,Chicago
-- SELECT * FROM test_schema.example_table; --