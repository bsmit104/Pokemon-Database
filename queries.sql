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

-- Show all data in the Type table
SELECT * FROM pokedex.Type;

-- Show all data in the Pokemon table
SELECT * FROM pokedex.Pokemon;

-- Show all data in the Move table
SELECT * FROM pokedex.Move;