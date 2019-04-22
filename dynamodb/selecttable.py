import boto3

ddb = boto3.resource('dynamodb', endpoint_url='http://localhost:9000')
table = ddb.Table('password')

# Print out some data about the table.
# This will cause a request to be made to DynamoDB and its attribute
# values will be set based on the response.
print(table.creation_date_time)
