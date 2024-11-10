import socket

def scan(target, ports):
    print("[*] Scanning Target: " + str(target))
    for port in range(1, ports):
        scan_port(target, port)

def scan_port(ipaddress, port):
     try:
         sock = socket.socket()
         sock.settimeout(1)
         sock.connect((ipaddress, port))
         service_name = socket.getservbyport(port)
         print("- Port Opened: " + str(port) + " | Service Running: " + service_name)
         sock.close()
     except socket.error:
                          pass

targets = input("Enter Target IP Addresses: ")
ports = int(input("Enter the number of ports: "))

if "," in targets:
    print("Scanning multiple Targets: ")
    for ip_address in targets.split(","):
        scan(ip_address.strip(' '), ports)
else:
        scan(targets , ports)