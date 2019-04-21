import boto3

ddb = boto3.resource('dynamodb', endpoint_url='http://localhost:9000')
table = ddb.Table('password')
response = table.scan()
item = response['Items']
print(item)
print(len(item))
