import boto3
import sys

shaone = sys.argv[1]
ddb = boto3.resource('dynamodb')
table = ddb.Table('password')
response = table.get_item(
    Key={
        'shaone': shaone,
    }
)
if 'Item' in response:
    item = response['Item']
    print(item)
