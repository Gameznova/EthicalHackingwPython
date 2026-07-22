#!/usr/bin/env python
"""47. Iterating Over Nested Data Structures"""
""" Handling user input
Questions for this assignment
Use the optparse library I showed you in the previous section to extend this program and make it take the IP range through a command line argument, let the argument be -t or --target, so users can call the program from terminal like so
python network_scanner.py --t 10.0.2.1/24
OR
python network_scanner.py --target 10.0.2.1/24"""

# Import scapy module as alias
import scapy.all as scapy
import optparse


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-t","--target",dest="target",help="Target IP range")
    (options, arguments) = parser.parse_args()

    if not options.target:
        parser.error("[-] Please specify a target IP range using -t or --target")

    return options


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request

    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    clients_list = []
    for element in answered_list:
        client_dict = {
            "ip": element[1].psrc,
            "mac": element[1].hwsrc
        }
        clients_list.append(client_dict)
    return clients_list


def print_result(results_list):
    print("IP\t\t\t\tMAC Address")
    print("----------------------------------")
    for client in results_list:
        print(client["ip"] + "\t\t" + client["mac"])


# Main execution
options = get_arguments()
scan_result = scan(options.target)
print_result(scan_result)

