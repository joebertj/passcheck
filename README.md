# passcheck

Check the strength of a password given data from major breaches. There are 551509767 items in total.

This started as DynamoDB only but it is too slow for me. It is an opportunity to casually compare with Cassandra using same data. Python filenames are kept the same for similar function.

Use `load.sh` to import data passing `dynamodb` or `cassandra` as first parameter and the directory of the raw data as the second parameter e.g `./load.sh cassandra ~/rawdata`.

## DynamoDB Local using Docker
Uses python and boto3 module to connect to a Local DynamoDB running on Docker.
To disable InMemory option:
`docker run -d -v ~/dynamodbdata:/home/dynamodblocal/data -p 9000:8000 amazon/dynamodb-local -Djava.library.path=./DynamoDBLocal_lib -jar DynamoDBLocal.jar -sharedDb -dbPath ./data`

## Apache Cassandra
Keyspace is unique for Cassandra. Think of it as "Database" in MySQL.
