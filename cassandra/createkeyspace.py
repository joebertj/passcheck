from cassandra.cluster import Cluster

cluster = Cluster()
session = cluster.connect()
session.execute("CREATE KEYSPACE user WITH replication = { 'class': 'SimpleStrategy', 'replication_factor': 1 } ")
print("Keyspace created")
