import boto3

ddb = boto3.resource('dynamodb')
table = ddb.Table('password')
response = table.scan()
if 'Items' in response:
    items = response['Items']
    print(len(items))
