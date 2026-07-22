#!/usr/bin/env python
"""40. Combing Frames to Broadcast Packets"""

# Import scapy module as alias
import scapy.all as scapy

# Define function to create arp request to broadcast MAC asking for IP
# We will design our own instead of using scapy.arping(ip)
def scan(ip):
    # Create a variable that holds an instance of an ARP packet object made by scapy
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    print("IP\t\t\t\tMAC Address\n----------------------------------")
    for element in answered_list:
        print(element[1].prsc + "\t\t" + element[1].hwsrc)
# Call scan function can router ip
# obtain router ip by > terminal > route -n
scan("192.168.1.1/24")

# Run script in terminal