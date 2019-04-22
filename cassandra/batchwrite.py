from cassandra.cluster import Cluster, BatchStatement

cluster = Cluster(['34.236.205.143'])
session = cluster.connect('user')
pstmt = session.prepare("INSERT INTO password (shaone,count) VALUES (?,?)")
i = 0
batch = BatchStatement()
f =  open('../test.data','r')
line = f.readline()
while line:
    i += 1
    (shaone,count) = line.split(':')
    batch.add(pstmt, (shaone,int(count)))
    line = f.readline()
    if i==4:
        i = 0
        session.execute(batch)
        batch = BatchStatement()
f.close()
#551509767
