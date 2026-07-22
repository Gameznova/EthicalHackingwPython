#!/usr/bin/env python
"""39 Using Scapy to Create an ARP Request"""
""" Goal > Discover clients on network
    Steps
    1. Create arp request directed to broadcast MAC asking for IP
    2. Send packet and receive response.
    3. Parse the response
    4. Print the result """

# Import scapy module as alias
import scapy.all as scapy

# Define function to create arp request to broadcast MAC asking for IP
# We will design our own instead of using scapy.arping(ip)
def scan(ip):
    # Create a variable that holds an instance of an ARP packet object made by scapy
    arp_request = scapy.ARP(pdst=ip)
    print(arp_request.summary()) # prints 0.0.0.0 so we need a way to set the IP to the value that we want

    """ use scapy.ls and enter the Class we want to learn the names of variables we can set for it"""
    # scapy.ls(scapy.ARP())
    """ prints:
     ARP who has 0.0.0.0 says 192.168.1.84
    hwtype     : XShortEnumField                     = 1               ('1')
    ptype      : XShortEnumField                     = 2048            ('2048')
    hwlen      : FieldLenField                       = None            ('None')
    plen       : FieldLenField                       = None            ('None')
    op         : ShortEnumField                      = 1               ('1')
    hwsrc      : MultipleTypeField (SourceMACField, StrFixedLenField) = '00:c0:ca:b2:80:0a' ('None')
    psrc       : MultipleTypeField (SourceIPField, SourceIP6Field, StrFixedLenField) = '192.168.1.84'  ('None')
    hwdst      : MultipleTypeField (MACField, StrFixedLenField) = '00:00:00:00:00:00' ('None')
    pdst       : MultipleTypeField (IPField, IP6Field, StrFixedLenField) = '0.0.0.0'       ('None')"""
    # we are interested in pdst so we add (pdst=ip) to arp_request variable

# Call scan function can router ip
# obtain router ip by > terminal > route -n
scan("192.168.1.1/24")

# Run script in terminal