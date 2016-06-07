import MySQLdb
import sys
import random

db = MySQLdb.connect("127.0.0.1", "root", "0007", "TESTDB")
cursor = db.cursor()


def dataPopulate(table, c1, c2, c3):
    query = "INSERT INTO " + table + "(c1, c2, c3)" \
            "VALUES(%s, %s, %s)"
    args = (c1, c2, c3)

    try:
        rows = cursor.execute(query, args)
        db.commit()
        print "Successfully commited =D"
    except TypeError:
        print "We got TypeError!"
    except:
        db.rollback()
        print "We got a problem! "
        print sys.exc_info()[0]

def getData(table):
    query = "select * from " + table
    rows = cursor.execute(query)
    data = cursor.fetchall()

    for row in data:
        print row

for i in range(100000):
    c1, c2, c3 = random.randint(0,50), random.randint(51,100), random.randint(101,200)

    dataPopulate("tableA", c1 , c2, c3)

    c1, c2, c3 = random.randint(0,50), random.randint(51,100), random.randint(101,200)

    dataPopulate("tableB", c1 , c2, c3)


# getData("tableA")

db.close()

print "Complete!"
