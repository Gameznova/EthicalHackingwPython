
#!/usr/bin/env python

# Import subprocess module and optparse for command-line arguments
import subprocess
import optparse

"""Parse the user input, and return the argument entered by the user"""

def get_arguments():
    # Variable holding OptionParser
    parser = optparse.OptionParser()
    # Add options to parser object
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    # Parse the user input - When you get called, return the information from where your called from.
    return parser.parse_args()

def change_mac(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])
    print("[+] Complete")

# Call function with options.[variable]
(options, arguments) = get_arguments()
change_mac(options.interface,options.new_mac)


# To run in Terminal > cd ~/PycharmProjects/1_MACaddressChanger > python 24_macReturnValuesfromFunc.py --i [interface] --m [new mac]