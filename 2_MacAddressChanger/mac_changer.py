#!/usr/bin/env python

# Import subprocess module
import subprocess
# Import optparse for command-line arguments
import optparse

# Variable holding OptionParser
parser = optparse.OptionParser()
# Add options to parser object
parser.add_option("-i", "--interface", dest="interface", help="Interface to change MAC address")
parser.add_option("-m", "--mac", dest="new_MAC", help="New MAC address")

# Obtain interface variable
interface = input("What interface do you want to use? ")

# Obtain mac variable and convert to appropiate format
mac = input("new MAC address (ex. 11:22:33:44:55:66): ").strip().upper()
# format MAC address if dashes, colons, or neither are used
clean = mac.replace(":","").replace("-","")
# Insert ":" every two characters
new_MAC = ":".join(clean[i:i+2] for i in range(0, len(clean), 2))
while len(new_MAC) > 18:
    mac = input("New MAC must be shorter: ")
print(f"Formatted MAC: {new_MAC}")

print("[+] Changing MAC address for " + interface)
print("\n")

# Simple MAC Address Changer
"""
subprocess.call(f"ifconfig {interface} down", shell=True)
subprocess.call(f"ifconfig {interface} hw ether {new_MAC}", shell=True)
subprocess.call(f"ifconfig {interface} up", shell=True)
"""

# 20. Handling User Input using a list of known elements to prevent injection
subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_MAC])
subprocess.call(["ifconfig", interface, "up"])
print("[+] Complete")

# Call ifconfig subprocess
subprocess.call(f"ifconfig {interface}", shell=True)

# To run in Terminal > cd ~/PycharmProjects/1_MACaddressChanger > python mac_changer,py