import boto3

ddb = boto3.resource('dynamodb', endpoint_url='http://localhost:9000')
table = ddb.Table('password')
response = table.get_item(
    Key={
        'shaone': '00000CA926DFCB1A4DD33AEFD2C2E029694507DB',
    }
)
item = response['Item']
print(item)
