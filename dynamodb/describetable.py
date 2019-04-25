import boto3

ddb = boto3.client('dynamodb')
response = ddb.describe_table(
	TableName='password'
)
print(response)
