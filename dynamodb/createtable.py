import boto3

ddb = boto3.resource('dynamodb', endpoint_url='http://localhost:9000')
table = ddb.create_table(
    TableName='password',
    KeySchema=[
        {
            'AttributeName': 'shaone',
            'KeyType': 'HASH'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'shaone',
            'AttributeType': 'S'
        }
    ],
	ProvisionedThroughput={
		'ReadCapacityUnits': 25,
		'WriteCapacityUnits': 25
	}
)

# Wait until the table exists.
table.meta.client.get_waiter('table_exists').wait(TableName='password')

# Print out some data about the table.
print(table.item_count)
