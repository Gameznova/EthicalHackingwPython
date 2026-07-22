
#!/usr/bin/env python

# Import subprocess module and optparse for command-line arguments
import subprocess
import optparse

# Variable holding OptionParser
parser = optparse.OptionParser()



# Add options to parser object
parser.add_option("-i", "--interface", dest="interface", help="Interface to change MAC address")
parser.add_option("-m", "--mac", dest="new_MAC", help="New MAC address")

print("[+] Changing MAC address for " + interface)
print("\n")


# 20. Handling User Input using a list of known elements to prevent injection
subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_MAC])
subprocess.call(["ifconfig", interface, "up"])
print("[+] Complete")

# Call ifconfig subprocess
subprocess.call(f"ifconfig {interface}", shell=True)

# To run in Terminal > cd ~/PycharmProjects/1_MACaddressChanger > python mac_changer,py