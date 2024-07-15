
----------------------------------
-- Insert Types into the types Table
INSERT INTO test_schema.types (typename)
SELECT DISTINCT type1 FROM test_schema.example_table
UNION
SELECT DISTINCT type2 FROM test_schema.example_table WHERE type2 IS NOT NULL;

-----------------------------------
-- Insert Data into the pokemon Table
INSERT INTO test_schema.pokemon (rownum, pokemonname, total, hp, attack, defense, specialatk, specialdef, speed, generation, legendary)
SELECT rownum, pokemonname, total, hp, attack, defense, specialatk, specialdef, speed, generation, legendary
FROM test_schema.example_table;

-----------------------------------
-- Insert Data into the pokemon_types Table
INSERT INTO test_schema.pokemon_types (pokemon_id, type_id)
SELECT DISTINCT p.id, t.id
FROM test_schema.example_table e
JOIN test_schema.pokemon p ON e.rownum = p.rownum
JOIN test_schema.types t ON e.type1 = t.typename;

INSERT INTO test_schema.pokemon_types (pokemon_id, type_id)
SELECT DISTINCT p.id, t.id
FROM test_schema.example_table e
JOIN test_schema.pokemon p ON e.rownum = p.rownum
JOIN test_schema.types t ON e.type2 = t.typename
WHERE e.type2 IS NOT NULL;