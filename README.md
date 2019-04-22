# passcheck

Check the strength of a password given data from major breaches. There are 551509767 items in total.

This is to casually compare DynamoDB with Cassandra using same data.

## DynamoDB Local using Docker
Uses python and boto3 module to connect to a Local DynamoDB running on Docker.
To disable InMemory option:
`docker run -d -v ~/dynamodbdata:/home/dynamodblocal/data -p 9000:8000 amazon/dynamodb-local -Djava.library.path=./DynamoDBLocal_lib -jar DynamoDBLocal.jar -sharedDb -dbPath ./data`

## Apache Cassandra
