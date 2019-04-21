import boto3
from itertools import islice

ddb = boto3.resource('dynamodb', endpoint_url='http://localhost:9000')
table = ddb.Table('password')
with table.batch_writer() as batch:
    for i in range(1000):
        with open('test.data') as f:
            line = next(islice(f, i, i + 1))
            (shaone,count) = line.split(':')
        batch.put_item(
            Item={
                'shaone': shaone,
                'count': count
            }
        )
