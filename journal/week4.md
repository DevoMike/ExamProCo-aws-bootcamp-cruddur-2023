# Week 4 — Postgres and RDS

I succesuccfully created an RDS instance called cruddur-db-instance in my amazon RDS platform
an End point was also created with avaliablity in My zone. London. 
the role is instance with engine postgreSQL. i selected the class
db.t3.micro



postgres installed.
db instance 
username: cruddurroot
master userPassword: Testing123a

dbname: cruddur
db: postgres
password: password

successfully RDS created




to access postgres from the Container env, run the code to enter postgres
psql -Upostgres --host localhost

create a database :
A new database called cruddur created using syntac
create database cruddur
a schema created to run some dababase querries

create a script called schema.sql to run a schema database
psql cruddur < db/schema.sql -h localhost -U postgres

TO export your connection_url use:
 export CONNECTION_URL="postgresql://postgres:password@localhost:5432/cruddur"

With the above syntac, you can connect to the database without providng password.


PSQL Commands
\x on -- expanded display when looking at data
\q -- Quit PSQL
\l -- List all databases
\c database_name -- Connect to a specific database
\dt -- List all tables in the current database
\d table_name -- Describe a specific table
\du -- List all users and their roles
\dn -- List all schemas in the current database
CREATE DATABASE database_name; -- Create a new database
DROP DATABASE database_name; -- Delete a database
CREATE TABLE table_name (column1 datatype1, column2 datatype2, ...); -- Create a new table
DROP TABLE table_name; -- Delete a table
SELECT column1, column2, ... FROM table_name WHERE condition; -- Select data from a table
INSERT INTO table_name (column1, column2, ...) VALUES (value1, value2, ...); -- Insert data into a table
UPDATE table_name SET column1 = value1, column2 = value2, ... WHERE condition; -- Update data in a table
DELETE FROM table_name WHERE condition; -- Delete data from a table

to quit postges, use \q.
script created successfully using psql cruddur < db/schema.sql -h localhost -U postgres

NOTEEEEEE::::REMEMBER TO REMOVE THE RDS INSTANCE CREATE IN AWS

create TABLE IN Postgres
successfully created a table
CREATE TABLE public.users (
  uuid UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
  display_name text,
  handle text
  cognito_user_id text,
  created_at TIMESTAMP default current_timestamp NOT NULL
);


With the seed.sql, data was successfully inserted into the table.
INSERT INTO public.users (display_name, handle, cognito_user_id)
VALUES
  ('Andrew Brown', 'andrewbrown' ,'MOCK'),
  ('Andrew Bayko', 'bayko' ,'MOCK');

INSERT INTO public.activities (user_uuid, message, expires_at)
VALUES




Working with the DBS
drive of postgres installed using the command pip install -r requirements.txt
after loading the file on the requirement attachment.










from psycopg_pool import ConnectionPool
import os

def query_wrap_object(template):
  sql = f"""
  (SELECT COALESCE(row_to_json(object_row),'{{}}'::json) FROM (
  {template}
  ) object_row);
  """
  return sql

def query_wrap_array(template):
  sql = f"""
  (SELECT COALESCE(array_to_json(array_agg(row_to_json(array_row))),'[]'::json) FROM (
  {template}
  ) array_row);
  """
  return sql

connection_url = os.getenv("CONNECTION_URL")
pool = ConnectionPool(connection_url)




