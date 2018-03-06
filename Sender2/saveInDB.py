import sqlite3
import sys
##Save Results in DB
def save(query):
    conn = sqlite3.connect('salar.db')
    print("Opened DB successfully :)")
        
    try:
        conn.execute(query);
        conn.commit()
        print("Saved in DB successfully :)")
    except:
        print("Error in save to DB :(\n"+str(sys.exc_info()))
        conn.rollback()
    conn.close()
    print("Closed DB successfully :)")
