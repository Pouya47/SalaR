import nmap
import sys,  getopt
from datetime import datetime 
from saveInDB import save
#Scan Target
target=''
#Scan Arguments
nmapArgs=' '
#Ports
#PORTS = [22,23,80,443,8080]
ports=''
#testID=1

###check command line Args
argv=sys.argv[1:]
#if (len(sys.argv)<2):
   # print 'Err1=> scan.py -t <target IP> [-p <Ports 80,443> -a <nmap args>] '
    #sys.exit()
 
try:
    opts, args = getopt.getopt(argv,"ht:p:a:",["ports=","args="])
except getopt.GetoptError:
    print 'Error=> scan.py -t <target IP> [-p <Ports 80,443> -a <nmap args>] '
    sys.exit(2)
    
for opt, arg in opts:
    if opt == '-h':
        print 'scan.py -t:<target IP> -[-p <Ports 80,443> -a <nmap args>]'
        sys.exit()
    elif opt in ("-t", "--target"):
         target = arg
    elif opt in ("-p", "--ports"):
         ports = arg
    elif opt in ("-a", "--args"):
         nmapArgs = arg


def nmscan(target, ports, nmArgs):
    PORTS=ports.split(',')
    #Remove Empty rows
    PORTS=filter(None, PORTS)
    #count ports
    if len(PORTS)==0:
        PORTS=65390
    else:
        PORTS=len(PORTS)
    
    portCmd=' -p '+ports
    
    nm = nmap.PortScanner()
    if(nmArgs=='' and ports==''):
        nm.scan(hosts=target)
    elif(nmArgs==''):
        nm.scan(hosts=target, arguments=portCmd)
    elif(ports==''):
        nm.scan(hosts=target, arguments='-'+nmArgs)
    else :
        nm.scan(hosts=target, arguments='-'+nmArgs+portCmd)
    print 'Used Command= '+nm.command_line()
    #print 'All hosts='+str(len(nm.all_hosts()))
         
    #Show results and count success rate
    success=0
    output=''
    startTime=datetime.now()
    
    for host in nm.all_hosts():
        print('----------------------------------------------------')
        print('Host : %s (%s)' % (host, nm[host].hostname()))
        print('State : %s' % nm[host].state())
        for proto in nm[host].all_protocols():
            print('----------')
            print('Protocol : %s' % proto)
     
            lport = nm[host][proto].keys()
            lport.sort()
            for port in lport:
                 #print ('port : %s\tstate : %s' % (port, nm[host][proto][port]['state']))
                 output+= 'port : %s\tstate : %s\n' % (port, nm[host][proto][port]['state'])
                 if nm[host][proto][port]['state']=='open':
                    success+=1
    print output
        
    succRate=0
            
    PORTS=PORTS*len(nm.all_hosts())
    #Success rate is percent from port of Live hosts not all hosts in command
    if len(nm.all_hosts())==0:#No live host found
        succRate=0
    else:
        succRate=100*success/PORTS*len(nm.all_hosts())
    
    print 'Scan success rate is '+str(succRate)+' %.'
    
    #Save Results
    sql = "INSERT INTO scanResults(startTime,endTime,target,command,openPorts,allPorts,sucessRate,result) \
           VALUES ('%s', '%s', '%s','%s', '%d','%d','%d', '%s' )" % \
           (startTime, datetime.now(), target, nm.command_line(),success, PORTS,  succRate,output )
    save(sql)

#nmscan(target, ports, nmapArgs)
