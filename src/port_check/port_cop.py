import socket
import os
import sys

def scan_port(ip, port):  
    try:  
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
        sock.settimeout(1)  
        result = sock.connect_ex((ip, port))  
        sock.close()  
        return result == 0  
    except:  
        return False  

target_ip = "localhost"  # Заменить на целевой IP  
ports_to_scan = [80, 443, 22, 21]  # Общие порты  
for port in ports_to_scan:  
    if scan_port(target_ip, port):  
        print(f"Port {port} is open")  
    else:  
        print(f"Port {port} is closed")  

input("Press Enter to continue")
os.system('cls' if os.name == 'nt' else 'clear')
os.execv(sys.executable, [sys.executable] + sys.argv)