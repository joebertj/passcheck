import psycopg2
from config import config
import sys

def insert_passwords(passwords):
    """ insert multiple passwords into the passwords table  """
    sql = "INSERT INTO password(shaone,count) VALUES(%s,%s) ON CONFLICT (shaone) DO NOTHING"
    conn = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.executemany(sql,passwords)
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    f =  open(sys.argv[1],'r')
    line = f.readline()
    lines = []
    while line:
        (shaone,count) = line.split(':')
        lines.append((shaone,int(count)))
        line = f.readline()
    insert_passwords(lines)
    f.close()
