-- Insert data into Type table
INSERT INTO Type (name) VALUES ('Fire'), ('Water'), ('Grass');

-- Insert data into Pokemon table
INSERT INTO Pokemon (name, type1, type2, hp, attack, defense, speed, generation)
VALUES ('Charmander', 1, NULL, 39, 52, 43, 65, 1);

-- Insert data into Move table
INSERT INTO Move (name, type_id, power, accuracy)
VALUES ('Ember', 1, 40, 100);