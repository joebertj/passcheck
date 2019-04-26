from cassandra.cluster import Cluster, BatchStatement
import sys

cluster = Cluster()
session = cluster.connect('user')
pstmt = session.prepare("INSERT INTO password (shaone,count) VALUES (?,?)")
i = 0
batch = BatchStatement()
f =  open(sys.argv[1],'r')
line = f.readline()
while line:
    i += 1
    (shaone,count) = line.split(':')
    batch.add(pstmt, (shaone,int(count)))
    line = f.readline()
    if i==2500:
        i = 0
        session.execute(batch)
        batch = BatchStatement()
f.close()
if i > 0:
    session.execute(batch)
