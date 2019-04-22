from cassandra.cluster import Cluster

cluster = Cluster()
session = cluster.connect()
session.set_keyspace('user')
session.execute("CREATE TABLE password (shaone varchar PRIMARY KEY, count int);")
print("Table created")
