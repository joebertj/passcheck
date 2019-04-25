from cassandra.cluster import Cluster

cluster = Cluster()
session = cluster.connect('user')
pstmt = session.prepare("SELECT count(*) FROM password")
row = session.execute(pstmt)[0]
print(row)
