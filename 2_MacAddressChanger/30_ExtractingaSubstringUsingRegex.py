#!/usr/bin/env python
""" 30. Extracting a Substring Using Regex
    Adding printouts of our results """

# Import modules
import subprocess
import optparse

# Import Regular Expression (re) module
import re

# Define Functions
def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to use")
    parser.add_option("-m", "--mac", dest="new_mac", help="MAC address to use")
    # options and arguments will contain the argumetns and values returned by parser.parse_args()
    (options, args) = parser.parse_args()
    # Check if the interface variable does not have a value, otherwise display error and exit
    if not options.interface:
        parser.error("[-] Please specify an interface")
    if not options.new_mac:
        parser.error("[-] Please specify a MAC address")
    # Handle the Code after the IF statement IF they've succesfully entered values
    # Return the options because we don't want to return arguments.
    return options

def change_mac(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

# create new variable options and
options = get_arguments()

# call change_mac function
# change_mac(options.interface, options.new_mac)

# Create variable to store the value
ifconfig_result = subprocess.check_output(["ifconfig", options.interface])
print(ifconfig_result)

# Use regex to filter our result
mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)

# Use an IF statement to provide an error if MAC cannot be read
if mac_address_search_result:
    # Print the result using group 0 to print only the first instance if multiple macs are within
    # (There should only be one MAC)
    print(mac_address_search_result.group(0))
else:
    print("[-] Could Not read MAC address")
