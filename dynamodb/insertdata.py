import boto3

ddb = boto3.resource('dynamodb', endpoint_url='http://localhost:9000')
table = ddb.Table('password')
table.put_item(
   Item={
        'shaone': '00000000DD7F2A1C68A35673713783CA390C9E93',
        'count': 630
    }
)
print(table)
