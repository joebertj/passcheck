from cassandra.cluster import Cluster

cluster = Cluster()
session = cluster.connect('user')
pstmt = session.prepare("INSERT INTO password (shaone,count) VALUES (%s,%s)")
batch = BatchStatement()
f =  open('../test.data','r')
line = f.readline()
while line:
    (shaone,count) = line.split(':')
    batch.add(pstmt, (shaone,count))
    line = f.readline()
f.close()
#551509767
