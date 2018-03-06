import commands

z= commands.getstatusoutput('nmap 127.0.0.1')
a= commands.getoutput('nmap 127.0.0.1')
#b= commands.getstatus('nmap 127.0.0.1')

#print z
print '='*40
print a
