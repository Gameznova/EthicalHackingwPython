#!/usr/bin/env python

""" Checks user inputs for validity"""
# import modules
import subprocess
import optparse

# Define functions
def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change MAC address")
    parser.add_option("-m", "--mac", dest = "new_mac", help = "New MAC address")
    # options and arguments will contain the argumetns and values returned by parser.parse_args()
    (options, arguments) = parser.parse_args()
    # Check if options.interface does NOT hold a value, otherwise show error
    if not options.interface:
        # Code to handle error
        # If the user did not enter an interface, we want to display an error and exit the program
        # If the user entered an interface, then we move to the next check
        parser.error("[-] Please specify an interface. Use --help for help for more information.")
    # Check if options.new_mac does NOT hold a value
    elif not options.new_mac:
        # Code to handle error
        parser.error("[-] Please specify a new mac. Use --help for help for more information.")
    # Handle the Code after the IF statement if they've succesfully entered values
    # Return options because we don't want to return arguments.
    return options

def change_mac(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface,  "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])
# create new variable options
options = get_arguments()
change_mac(options.interface,options.new_mac)