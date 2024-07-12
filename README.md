# Pokemon-Database
Refreshing my SQL knowledge


In order to get the full data loaded, run:
psql -U postgres -d pokemon -f testPokeSchema.sql
python testPoke.py
psql -U postgres -d pokemon
pokemon=# \encoding UTF8
pokemon=# SELECT * FROM test_schema.example_table;

In order to get selected columns of choice see example of simplifiedTableSchema.sql
to run it:
psql -U postgres -d pokemon -f simplifiedTableSchema.sql
python simplifiedTable.py
psql -U postgres -d pokemon
pokemon=# \encoding UTF8
pokemon=# SELECT * FROM test_schema.selected_columns_table;