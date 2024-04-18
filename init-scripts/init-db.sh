#!/bin/bash
set -e

# Run a SQL command
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    CREATE DATABASE neotourdb;
    CREATE USER neotouruser WITH PASSWORD '3277’
    CREATE ROLE neotouruser WITH LOGIN PASSWORD '3277';
    CREATE ROLE neotouruser WITH LOGIN PASSWORD '3277';
    ALTER ROLE neotouruser SET client_encoding TO 'utf8’;
    ALTER ROLE neotouruser SET default_transaction_isolation TO 'read committed';
    ALTER ROLE neotouruser SET timezone TO 'UTC';
    GRANT ALL PRIVILEGES ON DATABASE neotourdb TO neotouruser;
EOSQL

# You can also call SQL scripts
psql -v ON_ERROR_STOP=1 --username "neotouruser" --dbname "neotourdb" -f /docker-entrypoint-initdb.d/my_additional_setup.sql
