import boto3

ddb = boto3.resource('dynamodb', endpoint_url='http://localhost:9000')
table = ddb.Table('password')
response = table.get_item(
    Key={
        'shaone': '00000000DD7F2A1C68A35673713783CA390C9E93',
    }
)
item = response['Item']
print(item)
