import httplib
import time

def connect(url, port):
    try:
        user = httplib.HTTPConnection(url, port, timeout=5)
        #httplib.HTTPConnection('www.cwi.nl', 80, timeout=10)
        user.request("GET", "/")
        user.getresponse()
        return 'OK' 
        #print r1.status, r1.reason
    except Exception, exc:
        return exc   
        
def httpConnect(url, port, count):
    starttime = time.time()
    succes=0
    for i in range(1, count+1):
        #TODO: Need Asynchron
        result=connect(url,port)
        
        #try:
        if result=='OK':
                succes+=1
                print 'HTTP Connection '+str(i)+' was successfull.'
        else:
            print 'Error in HTTP req '+str(i)+' ,reason: '+str(result)
    
    
    endtime = time.time()
    elapsed = endtime - starttime
    print 'Total successfull HTTP Connections='+str(succes)+' from '+str(count)
    print 'Test duration (s)='+str(elapsed)
#TODO: Save rults in DB    
##Test   *************************************
ur="192.168.47.2"
httpConnect(ur, 80, 5)
