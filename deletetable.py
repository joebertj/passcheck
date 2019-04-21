import boto3

ddb = boto3.resource('dynamodb', endpoint_url='http://localhost:9000')
table = ddb.Table('password')
table.delete()
