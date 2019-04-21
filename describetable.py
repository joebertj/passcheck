import boto3

ddb = boto3.client('dynamodb', endpoint_url='http://localhost:9000')
response = ddb.describe_table(
	TableName='password'
)
print(response)
