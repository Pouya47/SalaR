#from--> https://wiki.python.org/moin/UdpCommunication
import socket
class colors:
#Colors class:
 #   reset all colors with colors.reset
  #  two subclasses fg for foreground and bg for background.
   # use as colors.subclass.colorname.
# i.e. colors.fg.red or colors.bg.green
   # also, the generic bold, disable, underline, reverse, strikethrough,
# and invisible work with the main class
   # i.e. colors.bold

    reset='\033[0m'
    bold='\033[01m'
    disable='\033[02m'
    underline='\033[04m'
    reverse='\033[07m'
    strikethrough='\033[09m'
    invisible='\033[08m'
    class fg:
        black='\033[30m'
        red='\033[31m'
        green='\033[32m'
        orange='\033[33m'
        blue='\033[34m'
        purple='\033[35m'
        cyan='\033[36m'
        lightgrey='\033[37m'
        darkgrey='\033[90m'
        lightred='\033[91m'
        lightgreen='\033[92m'
        yellow='\033[93m'
        lightblue='\033[94m'
        pink='\033[95m'
        lightcyan='\033[96m'
    class bg:
        black='\033[40m'
        red='\033[41m'
        green='\033[42m'
        orange='\033[43m'
        blue='\033[44m'
        purple='\033[45m'
        cyan='\033[46m'
        lightgrey='\033[47m'
msg=colors.fg.purple +colors.bold+'SalaR-> Single UDP Reciver program :{)'+colors.reset
msg2=colors.fg.cyan +'\nThis program listen to 1 connection and answer to it, then next one\nNo multithread'+colors.reset
print msg+msg2

HOST = "0.0.0.0"
port = 1395
 
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # UDP
sock.bind((HOST, port))
print 'Start Listen on IP '+HOST+':'+str(port)

while True:
	data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
	print 'Connected by ', addr
	print 'Received UDP message:', data
	sock.sendto('Salar reciver UDP: OK',addr)
