import socket

HOST = '0.0.0.0'
#HOST = socket.gethostname()
print 'Server program of SalaR, \nListen on IP '+HOST
PORTS = [22,23,80,443,8080]

s=[]

for i in range(len(PORTS)):
    s.append(socket.socket(socket.AF_INET, socket.SOCK_STREAM))
    s[i].bind((HOST, PORTS[i]))
    s[i].listen(1)
    print 'Listen on port '+str(PORTS[i])

while True:
    raw_input('Press Enter for exit:')
    print 'Bye'
    break;
#conn, addr = s.accept()

#print 'Connected by', addr

#while True:
#    data = conn.recv(1024)
#    print data;
#    #if not data: break
#    conn.send("Hello")
#    break;
#
#conn.close()

