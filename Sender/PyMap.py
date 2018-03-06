#from netaddr import *
#ip = IPNetwork('192.0.2.1/24')
#print ip.size

import nmap

nm = nmap.PortScannerAsync()
def callback_result(host, scan_result):
    print '------------------'
    print host, scan_result

nm.scan('192.168.1.1', arguments="-p 80", callback=callback_result)
while nm.still_scanning():
    print("Waiting >>>")
    nm.wait(2)
