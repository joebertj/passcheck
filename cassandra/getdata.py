from cassandra.cluster import Cluster
import sys
from cassandra.auth import PlainTextAuthProvider

auth_provider = PlainTextAuthProvider(
                username='cassandra', password='cassandra')
cluster = Cluster(auth_provider=auth_provider)
session = cluster.connect('user')
pstmt = session.prepare("SELECT * FROM password WHERE shaone=?")
shaone = []
shaone.append(sys.argv[1])
rows = session.execute(pstmt, shaone)
for row in rows:
    print(row)
