-- -- Select all Pokémon
-- SELECT * FROM Pokemon;

-- -- Select Pokémon by type
-- SELECT name FROM Pokemon
-- WHERE type1 = (SELECT id FROM Type WHERE name = 'Fire');

-- -- Join Pokémon with their types
-- SELECT Pokemon.name, Type.name AS type_name
-- FROM Pokemon
-- JOIN Type ON Pokemon.type1 = Type.id;

-- -- Find all Fire-type Pokémon with attack greater than 50
-- SELECT Pokemon.name
-- FROM Pokemon
-- JOIN Type ON Pokemon.type1 = Type.id
-- WHERE Type.name = 'Fire' AND Pokemon.attack > 50;


-- Show all data in the Pokemon table
SELECT * FROM pokedex.Pokemon;

-- Get pokemon by name
SELECT * FROM test_schema.example_table WHERE pokemonname = 'Pikachu';

-- Find average stats for each pokemon type
SELECT type1, AVG(total) AS avg_total, AVG(hp) AS avg_hp, AVG(attack) AS avg_attack,
       AVG(defense) AS avg_defense, AVG(specialatk) AS avg_specialatk,
       AVG(specialdef) AS avg_specialdef, AVG(speed) AS avg_speed
FROM test_schema.example_table
GROUP BY type1;

-- Find all legendary pokemon
SELECT * FROM test_schema.example_table WHERE legendary = TRUE;

-- Top 10 Pokémon by total stats
SELECT * FROM test_schema.example_table ORDER BY total DESC LIMIT 10;

-- Pokemon with type1 and type2 values
SELECT * FROM test_schema.example_table WHERE type2 IS NOT NULL;

-----------------------------------
-- NORMALIZED DATA
-----------------------------------

-- Fetch all Pokémon with their types
SELECT p.pokemonname, t.typename
FROM test_schema.pokemon p
JOIN test_schema.pokemon_types pt ON p.id = pt.pokemon_id
JOIN test_schema.types t ON pt.type_id = t.id;

-- Find average stats for a specific type
SELECT t.typename, AVG(p.total) AS avg_total, AVG(p.hp) AS avg_hp, AVG(p.attack) AS avg_attack, 
       AVG(p.defense) AS avg_defense, AVG(p.specialatk) AS avg_specialatk, 
       AVG(p.specialdef) AS avg_specialdef, AVG(p.speed) AS avg_speed
FROM test_schema.pokemon p
JOIN test_schema.pokemon_types pt ON p.id = pt.pokemon_id
JOIN test_schema.types t ON pt.type_id = t.id
WHERE t.typename = 'Fire'
GROUP BY t.typename;





-- Show all data in the Type table
-- SELECT * FROM pokedex.Type;

-- Show all data in the Move table
-- SELECT * FROM pokedex.Move;