import httplib
import time
from threading import Thread
from saveInDB import save

results=[]

def connect(url, port, index):
    try:
        user = httplib.HTTPConnection(url, port)
         #httplib.HTTPConnection('www.cwi.nl', 80, timeout=10)
        user.request("GET", "/")
        user.getresponse()
        results.append([index, 'OK'])
        #results[1].append('OK')
        
    except Exception, exc:
        results.append([index, str(exc)])
#        results[1].append()
        
def httpConnectAsync(url, port, count):
    starttime = time.time()
    succes=0
    faild=0
    #for clear prev results, this var is global must be clear at first
    del results[:]
    threads = []
    for i in range(1, count+1):
        thread = Thread(target=connect, args=(url, port, i))
        threads.append(thread)
        try:
            thread.start()
        except :
                print 'A thread cant start'
    for thread in threads:
        if thread.isAlive():
            thread.join()
     
    for  row in results:
        if row[1]=='OK':
                succes+=1
                print 'HTTP Connection '+str(row[0])+' was successfull.'
        else:
            faild+=1
            print 'Error in HTTP req '+str(row[0])+' ,reason: '+row[1]
    endtime = time.time()
    elapsed = endtime - starttime
    
    print 'Total successfull HTTP Connections='+str(succes)+' from '+str(count)
    print 'Test duration (s)='+str(elapsed)
    ##****** Save rults in DB  
    sql = "INSERT INTO `httpDosResults`(`url`,`port`,`faild`,`sucess`,`error`) \
           VALUES ('%s', '%d', '%d','%d','%d')" % \
           (url, port, faild, succes,count-succes-faild)
    save(sql)
    
    return succes
##Test   *************************************
#ur="127.0.0.1"
#ur="192.168.47.10"
#httpConnectAsync(ur, 80, 500)

#httpConnectAsync(ur, 80, 5)
