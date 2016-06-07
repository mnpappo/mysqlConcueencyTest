import MySQLdb
import sys

db = MySQLdb.connect("127.0.0.1", "root", "0007", "TESTDB")
cursor = db.cursor()


def crossProductTest():
    query = "select * from tableA,tableB"
    try:
        rows = cursor.execute(query)
        data = cursor.fetchall()
        counter = cursor.rowcount

        print "Total %d rows got!" % counter

    except:
        print sys.exc_info()[0]

    # for row in data:
    #     print row


def joinTest():
    query = "select * from tableA join tableB"
    rows = cursor.execute(query)
    data = cursor.fetchall()
    counter = cursor.rowcount

    # for row in data:
    #     print row

    return rowcount


crossProductTest()
print "Cross Product Test successfull"


# joinTest()
# print "Join Test successfull"

db.close()


print "Complete!"
