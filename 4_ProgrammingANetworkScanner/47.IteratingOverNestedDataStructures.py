#!/usr/bin/env python
"""47. Iterating Over Nested Data Structures"""

# Import scapy module as alias
import scapy.all as scapy
import optparse

# Define function to create arp request to broadcast MAC asking for IP
# We will design our own instead of using scapy.arping(ip)
def scan(ip):
    # Create a variable that holds an instance of an ARP packet object made by scapy
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    clients_list = []
    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        clients_list.append(client_dict)
    return clients_list

def print_result(results_list):
    print("IP\t\t\t\tMAC Address\n----------------------------------")
    # for each element in the results, we should get the dictionaries with their keys and values
    for client in results_list:
        print(client["ip"] + "\t\t" + client["mac"])

# Capture value from the scan function
scan_result = scan("192.168.1.1/24")
print(scan_result)
# Run script in terminal