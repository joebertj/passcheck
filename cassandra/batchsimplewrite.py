from cassandra.cluster import Cluster

cluster = Cluster(['34.236.205.143'])
session = cluster.connect('user')
pstmt = session.prepare("INSERT INTO password (shaone,count) VALUES (?,?)")
f =  open('../test.data','r')
line = f.readline()
while line:
    (shaone,count) = line.split(':')
    session.execute(pstmt, (shaone,int(count)))
    line = f.readline()
f.close()
#551509767
