import MySQLdb
import sys

db = MySQLdb.connect("127.0.0.1", "root", "0007", "TESTDB")
cursor = db.cursor()

def iter_row(cursor, size=10):
    while True:
        rows = cursor.fetchmany(size)
        if not rows:
            break
        for row in rows:
            yield row

def crossProductTest():
    query = "select * from tableB, tableA LIMIT 0, 150000"
    try:
        rows = cursor.execute(query)

        for row in iter_row(cursor, 150000):
            print(row)

        # data = cursor.fetchall()

        # statement = cursor.statement

        counter = cursor.rowcount
        print "Total %s rows got!" % counter
        # print "The statement is: %s" % statement

        print "Cross Product Test successfull"

    except:
        print "Error!!!"
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


# joinTest()
# print "Join Test successfull"

db.close()


print "Complete!"
