# passcheck

Check the strength of a password given data from major breaches. There are 551509767 items in total.

This started as DynamoDB only but it is too slow for me. It is an opportunity to casually compare with Cassandra using same data. PostgreSQL was added eventually. Python filenames are kept the same for similar function.

Use `load.sh` to import data passing `dynamodb`, `cassandra` or `postgresql`  as first parameter and the directory of the raw data as the second parameter e.g `./load.sh cassandra ~/rawdata`.

## DynamoDB Local using Docker
Uses python and boto3 module to connect to a Local DynamoDB running on Docker.
To disable InMemory option:
`docker run -d -v ~/dynamodbdata:/home/dynamodblocal/data -p 9000:8000 amazon/dynamodb-local -Djava.library.path=./DynamoDBLocal_lib -jar DynamoDBLocal.jar -sharedDb -dbPath ./data`

## Apache Cassandra
Keyspace is unique for Cassandra. Think of it as "Database" in MySQL.

## PostgreSQL
1. Switch to postgres user
`sudo su postgres`
2. Enter the the interactive terminal for working with Postgres
`psql`
3. Create the database (change databasename)
`CREATE DATABASE databasename;`
4. Create user (change myusername and mypassword)
`CREATE USER myusername WITH PASSWORD 'mypassword';`
5. Grant privileges on database to user
`GRANT ALL PRIVILEGES ON DATABASE "databasename" to myusername;`
6. Create file `database.ini` in postgresql folder with the following contents:
```
[postgresql]
host=localhost
database=databasename
user=myusername
password=mypassword
```
