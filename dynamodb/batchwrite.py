import boto3
from itertools import islice
import sys

ddb = boto3.resource('dynamodb')
table = ddb.Table('password')
f =  open(sys.argv[1],'r')
line = f.readline()
#with table.batch_writer(overwrite_by_pkeys=['shaone']) as batch:
with table.batch_writer() as batch:
	while line:
		(shaone,count) = line.split(':')
		batch.put_item(
			Item={
				'shaone': shaone,
				'count': count
			}
		)
		line = f.readline()
f.close()
