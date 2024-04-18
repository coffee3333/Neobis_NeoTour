-- -- Create a database
-- CREATE DATABASE neotourdb;

-- -- Create a database user
-- CREATE USER neotouruser WITH PASSWORD '3277';


-- -- Set permissions
-- GRANT ALL PRIVILEGES ON DATABASE neotourdb TO neotouruser;

-- -- Switch to the new database
-- \c neotourdb;

-- -- Create a table
-- CREATE TABLE users (
--     id SERIAL PRIMARY KEY,
--     username VARCHAR(255) UNIQUE NOT NULL,
--     created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
-- );

-- -- Insert initial data
-- INSERT INTO users (username) VALUES ('admin');


CREATE DATABASE neotourdb;
CREATE USER neotouruser WITH PASSWORD '3277';
CREATE ROLE neotouruser WITH LOGIN PASSWORD '3277';
ALTER ROLE neotouruser SET client_encoding TO 'utf8';
ALTER ROLE neotouruser SET default_transaction_isolation TO 'read committed';
ALTER ROLE neotouruser SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE neotourdb TO neotouruser;