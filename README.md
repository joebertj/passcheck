# passcheck

Check the strength of a password given data from major breaches.

This started as DynamoDB only but it is too slow for me. It is an opportunity to casually compare with Cassandra using same data. PostgreSQL was added eventually. Python filenames are kept the same for similar function.

Use `load.sh` to import data passing `dynamodb`, `cassandra` or `postgresql`  as first parameter and the directory of the raw data as the second parameter e.g `./load.sh cassandra ~/rawdata`.

Extract password data from [haveibeenpwned](https://haveibeenpwned.com/Passwords) on the rawdata folder. There are 551509767 items in total. For me, I `split` the data so it is easy to resume and not waste time on already completed data if the connection or script is interrupted e.g. `split -l 1000000 <filename> <prefix>`. Since the second parameter is actually a directory then the script will load all files placed there. You can generate your own data files as long as the format is colon (:) separated with the first value a SHA1 of a password and the second value the frequency (count of password breach) .e.g. 7C4A8D09CA3762AF61E59520943DC26494F8941B:123456

## DynamoDB
Uses python and boto3 module to connect to a DynamoDB.

### AWS DynamodDB
- Install `awscli` e.g. `sudo apt install awscli` for Ubuntu/Debian
- Install boto3 e.g. `sudo apt install python-boto3`

Use this code for client and resource:
```
boto3.client('dynamodb')
boto3.resource('dynamodb')
```

### Local DynamoDB running on Docker

I used port 9000. Default is 8000.

Use this code for client and resource:
```
boto3.client('dynamodb', endpoint_url='http://localhost:9000')
boto3.resource('dynamodb', endpoint_url='http://localhost:9000')
```
To disable InMemory option:
`docker run -d -v ~/dynamodbdata:/home/dynamodblocal/data -p 9000:8000 amazon/dynamodb-local -Djava.library.path=./DynamoDBLocal_lib -jar DynamoDBLocal.jar -sharedDb -dbPath ./data`

## Apache Cassandra
Keyspace is unique for Cassandra. Think of it as "Database" in PostgreSQL. Local default installation should work.

## PostgreSQL
Uses psycopg2 and configreader module. To install, `sudo apt install python-psycopg2 python-configreader`.

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
6. Create file `database.ini` with the following contents:
```
[postgresql]
host=localhost
database=databasename
user=myusername
password=mypassword
```
Run your scripts in the same directory where database.ini is.

## Checking a password against the database
Use `checkpass.sh` to check a password against the database. The first parameter is the same as `load.sh`. The second parameter is the password itself. e.g. `./checkpass.sh cassandra god`
