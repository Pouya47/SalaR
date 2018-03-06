from scapy.all import *

A = '192.168.100.100' # spoofed source IP address
B = '100.0.0.1' # destination IP address
C = 10000 # source port
D = 80 # destination port
payload = "yada yada yada" # packet payload

spoofed_packet = IP(src=A, dst=B) / TCP(sport=C, dport=D) / payload
send(spoofed_packet)
