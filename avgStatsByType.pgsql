CREATE OR REPLACE FUNCTION test_schema.avg_stats_by_type(p_type VARCHAR)
RETURNS TABLE(
    avg_total INTEGER,
    avg_hp INTEGER,
    avg_attack INTEGER,
    avg_defense INTEGER,
    avg_specialatk INTEGER,
    avg_specialdef INTEGER,
    avg_speed INTEGER
) AS $$
BEGIN
    RETURN QUERY
    SELECT AVG(total) AS avg_total, AVG(hp) AS avg_hp, AVG(attack) AS avg_attack, 
           AVG(defense) AS avg_defense, AVG(specialatk) AS avg_specialatk, 
           AVG(specialdef) AS avg_specialdef, AVG(speed) AS avg_speed
    FROM test_schema.example_table
    WHERE type1 = p_type OR type2 = p_type;
END;
$$ LANGUAGE plpgsql;


-- usage example
-- psql -U postgres -d pokemon
-- SELECT * FROM test_schema.avg_stats_by_type('Fire');