#!/usr/bin/env python
"""37. Introduction ARP scapy"""
""" Uses scapy and arp to scan all clients on the same network"""

# Import scapy module as alias
import scapy.all as scapy

# Define function to scan using an ip address as an argument
def scan(ip):
    # address resolution ping
    scapy.arping(ip)

# Call scan function with the router's gateway ip
# find IP: terminal > route -n
scan("192.168.1.1/24")
