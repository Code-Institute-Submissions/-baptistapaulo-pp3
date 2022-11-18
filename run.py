# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import pyfiglet
import os

# Welcome Message
logo = pyfiglet.figlet_format("IP Subnetting")
print(logo)
print("Welcome to the 'IP Subnet Calculator' tool.\n")
print("This tool pretends to help engineers on their "
      "daily support tasks or projects.\n")
print("Engineers will be able to:\n")
print("- calculate available IPs\n")
print("- determine subnet range\n")
print("- generate a random IP\n")

# Clear Terminal
os.system('cls' if os.name == 'nt' else 'clear')