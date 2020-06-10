#!/usr/bin/env python3

from cassandra import ConsistencyLevel
from cassandra.cluster import Cluster
from cassandra.query import BatchType, SimpleStatement
from ssl import SSLContext, PROTOCOL_TLSv1, CERT_REQUIRED
from cassandra.auth import PlainTextAuthProvider
import sys, os

ssl_context = SSLContext(PROTOCOL_TLSv1)
ssl_context.load_verify_locations('./AmazonRootCA1.pem')
ssl_context.verify_mode = CERT_REQUIRED
auth_provider = PlainTextAuthProvider(username=os.getenv('USER'), password=os.getenv('PASS'))
cluster = Cluster(['cassandra.us-west-2.amazonaws.com'], ssl_context=ssl_context, auth_provider=auth_provider, port=9142)
session = cluster.connect('user')
pstmt = session.prepare("INSERT INTO password (shaone,count) VALUES (?,?)")
pstmt.consistency_level = ConsistencyLevel.LOCAL_QUORUM 
f =  open(sys.argv[1],'r')
line = f.readline()
while line:
    (shaone,count) = line.split(':')
    session.execute(pstmt, (shaone, int(count)))
    line = f.readline()
f.close()
