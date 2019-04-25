from cassandra.cluster import Cluster
import sys

cluster = Cluster()
session = cluster.connect('user')
pstmt = session.prepare("SELECT * FROM password WHERE shaone=?")
shaone = []
shaone.append(sys.argv[1])
rows = session.execute(pstmt, shaone)
for row in rows:
    print(row)
