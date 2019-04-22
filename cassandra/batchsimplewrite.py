from cassandra.cluster import Cluster
import sys

cluster = Cluster(['34.236.205.143'])
session = cluster.connect('user')
pstmt = session.prepare("INSERT INTO password (shaone,count) VALUES (?,?)")
f =  open(sys.argv[1],'r')
line = f.readline()
while line:
    (shaone,count) = line.split(':')
    session.execute(pstmt, (shaone,int(count)))
    line = f.readline()
f.close()
#551509767
