#!/usr/bin/python3

'''
a script that lists all states
from the database
'''

if __name__ == "__main__":


    import MySQLdb
    from sys import argv

    conect = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                             passwd=argv[2], db=argv[3], charset="utf8")
    cursor = conect.cursor()
cursor.execute("SELECT * FROM states ORDER BY id ASC") # HERE I have to know SQL to grab all states in my database
query_rows = cursor.fetchall()
for row in query_rows:
    print(row)
cursor.close()
db.close()
