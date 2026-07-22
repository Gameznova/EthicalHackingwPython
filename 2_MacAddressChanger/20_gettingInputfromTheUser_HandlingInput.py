
#!/usr/bin/env python

# Import subprocess module and optparse for command-line arguments
import subprocess
import optparse

# Variable holding OptionParser
parser = optparse.OptionParser()

# Add options to parser object
parser.add_option("-i", "--interface", dest="interface", help="Interface to change MAC address")
parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")

# Allows the object to understand what the user has put in
(options, arguments) = parser.parse_args()

# Change variables to accept Options
interface = options.interface
new_mac = options.new_mac

print("[+] Changing MAC address for " + interface)
print("\n")


# 20. Handling User Input using a list of known elements to prevent injection
subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])
print("[+] Complete")



# To run in Terminal > cd ~/PycharmProjects/1_MACaddressChanger > python 20_getingInput... --i [interface] --m [new mac]