from cassandra.cluster import Cluster

cluster = Cluster()
session = cluster.connect('user')
session.execute("INSERT INTO password (shaone,count) VALUES (%s,%s)",("00000000DD7F2A1C68A35673713783CA390C9E93",360))
pstmt = session.prepare("SELECT * FROM password WHERE shaone=?")
row = session.execute(pstmt, ["00000000DD7F2A1C68A35673713783CA390C9E93"])[0]
print(row)
