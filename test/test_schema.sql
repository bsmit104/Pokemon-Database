DROP SCHEMA IF EXISTS test_schema CASCADE;
CREATE SCHEMA test_schema;

CREATE TABLE test_schema.example_table (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    age INTEGER,
    city VARCHAR(50)
);

-- SELECT * FROM test_schema.example_table; --