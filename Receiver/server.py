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
msg=colors.fg.yellow +colors.bold+'SalaR Server program :{)'+colors.reset

HOST = '0.0.0.0'
#HOST = socket.gethostname()
print msg+'\nListen on IP '+HOST
PORTS = [443,8080]


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


