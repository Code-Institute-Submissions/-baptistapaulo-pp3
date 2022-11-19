# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import pyfiglet
import os
import time


def cls_terminal():
    """
    Clear terminal with os.system
    https://stackoverflow.com/questions/2084508/clear-terminal-in-python
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def dec2bin(integer):
    """
    Convert IP address string to binary
    https://stackoverflow.com/questions/2733788/convert-ip-address-string-to-binary-in-python
    """
    binary = '.'.join([bin(int(x)+256)[3:] for x in integer.split('.')])
    return binary

def complement(number):
    if number == '0':
        number = '1'
    elif number == '.':
        pass
    else:
        number = '0'
    return number

def find_wildcard(binary_subnet):
    binary_list = list(binary_subnet)
    wildcard = ''.join(complement(binary_list[y]) for y in range(len(binary_list)))
    return wildcard

def convert_decimal(wildcard_Binary):
    binary = {}
    for x in range(4):
        binary[x] = int(wildcard_Binary.split(".")[x], 2)
    dec = ".".join(str(binary[x]) for x in range(4))
    return dec

def menu():
    """
    List the options to be selected by engineers.
    """
    while True:
        option = input(
            "[1] Calculate available IPs\n"
            "[2] Determine subnet range\n"
            "[3] Generate a random IP\n"
        )
        if option == '1':
            cls_terminal()
            choice1()
            break
        if option == '2':
            cls_terminal()
            choice2()
            break
        else:
            cls_terminal()
            choice3()
            break




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
input("Press Enter to continue...")
cls_terminal()
# Query's Message for Data
logo = pyfiglet.figlet_format("IP Subnetting")
print(logo)
print("Provide the following details.\n")
ip = input("Enter the NETWORK [x.x.x.x]: ")
subnet = input("Enter the MASK [y.y.y.y]: ")
input("\nPress Enter to continue...")
cls_terminal()
# Option's Message
logo = pyfiglet.figlet_format("IP Subnetting")
print(logo)
print("Which option would you like to select?\n")
menu()
ip_binary = dec2bin(ip)
subnet_binary = dec2bin(subnet)
print('\nIP:', IP, "->", ip_binary)
print('Subnet:', Subnet, "->", subnet_binary)
wildcard_binary = find_wildcard(dec2bin(Subnet))
WildCard = convert_decimal(wildcard_binary)
print('Wildcard:', WildCard, '->', wildcard_binary)