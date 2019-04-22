import boto3

ddb = boto3.client('dynamodb', endpoint_url='http://localhost:9000')
table = ddb.update_table(
    TableName='password',
    AttributeDefinitions=[
        {
            'AttributeName': 'shaone',
            'AttributeType': 'S'
        }
    ],
	ProvisionedThroughput={
		'ReadCapacityUnits': 25,
		'WriteCapacityUnits': 30000
	}
)

