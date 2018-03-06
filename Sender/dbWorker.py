import sqlite3
import sys

def connect_db(query):
    #"""Connects to the database. and run query on it, return curser"""
    try:
        with open('salar.db'): pass
    except IOError as io:
        print "DB file dosn't exists. {0}".format(io)
        sys.exit(1)
    try:
        conn = sqlite3.connect('salar.db')
        cur = conn.cursor()
        cur.execute(query)
        return cur
    except:
        print "Error in connect_db. ",  sys.exc_info()
        sys.exit(1)
    #finally:
     #   if conn:
        #    conn.close()

##*************** Never do this -- insecure! ***************
#symbol = 'RHAT'
#c.execute("SELECT * FROM stocks WHERE symbol = '%s'" % symbol)
# Do this instead
#t = ('RHAT',)
#c.execute('SELECT * FROM stocks WHERE symbol=?', t)
##************** End hint **********************************

#print connect_db("select * from scanResults").fetchall()
