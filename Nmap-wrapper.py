import os
ip = input("Enter IP/Subnet to scan: ")
os.system(f"nmap -sV {ip} -oN scan.txt")
