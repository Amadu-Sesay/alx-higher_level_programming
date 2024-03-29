#!/usr/bin/python3
""" script that lists all states with a name starting with N
(upper N) from the database hbtn_0e_0_usa"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost',
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         port=3306)
    """In order to put our new connnection to good use we
     need to create a cursor object"""
    cursor = db.cursor()
    """The execute function requires one parameter, the query."""
    cursor.execute("SELECT * FROM states\
        WHERE name REGEXP BINARY '^N'\
            ORDER BY id ASC")
    """Obtaining Query Results"""
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    """ Close all cursors"""
    cursor.close()
    """Close all databases"""
    db.close()
