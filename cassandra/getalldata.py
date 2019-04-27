from cassandra.cluster import Cluster
from cassandra.cluster import ExecutionProfile

cluster = Cluster()
session = cluster.connect('user')
row = session.execute("SELECT count(*) FROM password")
print(row)
