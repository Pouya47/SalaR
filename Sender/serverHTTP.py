import SocketServer
from SimpleHTTPServer import SimpleHTTPRequestHandler
import signal
import BaseHTTPServer

PORT = 80
#server run time in secound
runTime=500
 #recive requests counter
count=[]


class ThreadingSimpleServer(SocketServer.ThreadingMixIn,
                   BaseHTTPServer.HTTPServer):
    pass


class myResponse(SimpleHTTPRequestHandler):
    def do_GET(self):
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            #Response text can be a file or fix or random string
            self.wfile.write('Hello')
            count.append(self.client_address[0])
            #TODO: save request time
            return 


#for Handle exit signal
def handler(signum, frame):
    print "HTTP Server Stopped!"
    raise Exception("end of time")
 
 
def serverHttp():
            #Thread base serving for performance
        httpd=ThreadingSimpleServer(('', PORT), myResponse)
        while 1:
            httpd.handle_request()        


def startHttpServer():
    print 'serving at port %d for %d secound ...' %(PORT,  runTime)
    signal.signal(signal.SIGALRM, handler)
    # Define a timeout for your function in secound
    signal.alarm(runTime) 
    #count=0
    try:
        serverHttp()
    except Exception, exc:
        print exc
        
    finally:
        print count
        print 'Total succesfull requests='+str(len(count))
        #TODO: save results in DB
        return len(count)
        
##***********************Test*****************
startHttpServer()
