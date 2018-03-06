import nmap
nm = nmap.PortScanner()
x= nm.scan('127.0.0.1', '80')
print x
print '='*40
print nm.command_line()
#'nmap -oX - -p 22-443 -sV 127.0.0.1'
print '='*40
print nm.scaninfo()

print nm.csv()
