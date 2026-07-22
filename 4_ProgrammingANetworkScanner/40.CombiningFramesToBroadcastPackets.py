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
    print(arp_request_broadcast.summary())
    arp_request_broadcast.show()


# Call scan function can router ip
# obtain router ip by > terminal > route -n
scan("192.168.1.1/24")

# Run script in terminal