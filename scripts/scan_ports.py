import sys
import socket
import pyfiglet
import threading

ascii_banner = pyfiglet.figlet_format("TryHackMe \n Python 4 Pentesters \nPort Scanner")
print(ascii_banner)

ip = '192.168.1.6' 
open_ports =[] 

ports = range(1, 65535)

def probe_port(ip, port, result = 1):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.1)
        res = sock.connect_ex((ip, port))
        if res == 0:
            result = 0
        sock.close()
    except Exception as e:
        pass
    return result

for port in ports:
    sys.stdout.flush()
    print(f"Probing port {port}...")
    res = probe_port(ip, port)
    if res == 0:
        open_ports.append(port)

if open_ports: 
  print ("Open Ports are: ") 
  print (sorted(open_ports)) 
else: 
  print ("Looks like no ports are open :(")
