import boto3

# For a Boto3 client.
ddb = boto3.client('dynamodb', endpoint_url='http://localhost:9000')
response = ddb.list_tables()
print(response)
