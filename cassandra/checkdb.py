from cassandra.cluster import Cluster

cluster = Cluster()
session = cluster.connect()
rows = session.execute("SELECT keyspace_name FROM system_schema.keyspaces")
print("Keyspaces")
for row in rows:
    print(row[0])
