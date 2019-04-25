import psycopg2
from config import config
import sys

def select_shaone():
    sql = "SELECT count from password WHERE shaone='E814E2A504944BA2979456BD502EFCDEBD97BC64'"
    conn = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql)
        row = cur.fetchone()
        while row is not None:
            print(row[0])
            row = cur.fetchone()
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
    select_shaone()
