import boto3

ddb = boto3.resource('dynamodb', endpoint_url='http://localhost:9000')
table = ddb.Table('password')
table.put_item(
   Item={
        'shaone': '4e1243bd22c66e76c2ba9eddc1f91394e57f9f83',
        'count': 1
    }
)
print(table)
