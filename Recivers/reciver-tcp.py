import socket
import sys
import signal

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
msg=colors.fg.yellow +colors.bold+'SalaR-> Single TCP Reciver program :{)'+colors.reset
msg2=colors.fg.red +'\nThis program listen to 1 connection and answer to it, then next one\nNo multithread'+colors.reset
print msg+msg2

HOST = '0.0.0.0' # Symbolic name meaning all available interfaces
port = 1395     

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Listen to TCP 

s.bind((HOST, port))
print 'Start Listen on IP '+HOST+':'+str(port)
count=0


#Close listen after exit
def exit_handler(signal, frame):
        print('You pressed Ctrl+C!')
        s.close()
        sys.exit(0)
        
signal.signal(signal.SIGINT, exit_handler)
print('Press Ctrl+C for exit')
#signal.pause()



while True:
	print 'Wait for a connection on '+HOST+':'+str(port)
	
	s.listen(1)
	conn, addr = s.accept()
	print 'Connected by ', addr
	count=count+1
	print 'Connection count ',count
	
	while True:

		try:
			data = conn.recv(1024)

			if not data: break

			print "Client Says: "+data
			conn.sendall("Salar reciver: OK")

		except socket.error:
			print "Error Occured."
			s.close()
			break




