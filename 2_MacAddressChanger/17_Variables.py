#!/user/bin/env python

import subprocess

# Define Variables
interface = "eth0"
new_MAC = "00:11:AB:MG:44:55"

# Change Mac
subprocess.call(f"ifconfig {inferface} down", shell=True)
subprocess.call(f"ifconfig {inferface} hw ether {new_MAC}", shell=True)
subprocess.call("ifconfig {interface} up", shell=True)


