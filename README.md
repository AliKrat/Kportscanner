# Kportscanner
A simple Python-based port scanner that allows users to scan multiple IP addresses and check for open ports within a specified port range. Additionally, the tool provides the names of the services running on those open ports using service detection.

Features:
-> Scan a range of IP addresses to identify which ports are open.
-> User-specified port range allows flexibility in scanning.
-> Service detection to display the service name for each open port (e.g., HTTP for port 80).
-> Easy-to-use command-line interface for interacting with the tool.

Prerequisites:
-> Python 3.x
-> Internet connection to scan remote IPs
-> Some ports may be blocked or filtered by firewalls, affecting results

Example Usage:
python3 port_scanner.py

The program will ask you for:

-> IP Address or Range of IPs: You can specify one or more IP addresses to scan.
-> Port Range: Define the range of ports (e.g., 20-80 to scan ports from 20 to 80).

Once the scan is complete, it will display:
-> Which ports are open on the target IP(s).
-> Service names for the open ports (such as HTTP, FTP, SSH, etc.).
