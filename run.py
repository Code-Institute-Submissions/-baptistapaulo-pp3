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
