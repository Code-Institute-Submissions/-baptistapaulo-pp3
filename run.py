import pyfiglet
import os


def cls_terminal():
    """
    Clear terminal with os.system
    https://stackoverflow.com/questions/2084508/clear-terminal-in-python
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def dec2bin(integer):
    """
    Convert IP address string to binary 
    https://stackoverflow.com/questions/2733788/
    convert-ip-address-string-to-binary-in-python
    """
    binary = '.'.join([bin(int(x)+256)[3:] for x in integer.split('.')])
    return binary

# Wildcard Mask


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
    wildcard = ''.join(complement(binary_list[y])
                       for y in range(len(binary_list)))
    return wildcard


def convert_decimal(wildcard_Binary):
    binary = {}
    for x in range(4):
        binary[x] = int(wildcard_Binary.split(".")[x], 2)
    dec = ".".join(str(binary[x]) for x in range(4))
    return dec

# Network ID


def andOP(IP1, IP2):
    ID_list = {}
    for y in range(4):
        ID_list[y] = int(IP1.split(".")[y]) & int(IP2.split(".")[y])
    ID = ".".join(str(ID_list[z]) for z in range(4))
    return ID

# Broadcast IP


def orOP(IP1, IP2):
    Broadcast_list = {}
    for z in range(4):
        Broadcast_list[z] = int(IP1.split(".")[z]) | int(IP2.split(".")[z])
    broadcast = ".".join(str(Broadcast_list[c]) for c in range(4))
    return broadcast

# Max IP


def maxiIP(brdcstIP):
    maxIPs = brdcstIP.split(".")
    if int(brdcstIP.split(".")[3]) - 1 == 0:
        if int(brdcstIP.split(".")[2]) - 1 == 0:
            if int(brdcstIP.split(".")[1]) - 1 == 0:
                maxIPs[0] = int(brdcstIP.split(".")[0]) - 1
            else:
                maxIPs[1] = int(brdcstIP.split(".")[1]) - 1
        else:
            maxIPs[2] = int(brdcstIP.split(".")[2]) - 1
    else:
        maxIPs[3] = int(brdcstIP.split(".")[3]) - 1
    return ".".join(str(maxIPs[x]) for x in range(4))

# Min IP


def miniIP(ntwrkID):
    miniIPs = ntwrkID.split(".")
    if int(ntwrkID.split(".")[3]) + 1 == 256:
        if int(ntwrkID.split(".")[2]) + 1 == 256:
            if int(ntwrkID.split(".")[1]) + 1 == 256:
                miniIPs[0] = int(ntwrkID.split(".")[0]) + 1
                miniIPs[1] = 0
                miniIPs[2] = 0
                miniIPs[3] = 0
            else:
                miniIPs[1] = int(ntwrkID.split(".")[1]) + 1
                miniIPs[2] = 0
                miniIPs[3] = 0
        else:
            miniIPs[2] = int(ntwrkID.split(".")[2]) + 1
            miniIPs[3] = 0
    else:
        miniIPs[3] = int(ntwrkID.split(".")[3]) + 1
    return ".".join(str(miniIPs[x]) for x in range(4))


def menu():
    """
    List the options to be selected by engineers.
    """
    option = input(
        "[1] Calculate available IPs\n"
        "[2] Determine subnet range\n"
        "[3] Generate a random IP\n"
    )

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
networkID = andOP(IP, Subnet)
network_Binary = dec2bin(networkID)
print('Network ID:', networkID, "->", network_Binary)
broadcastIP = orOP(networkID, WildCard)
broadcastIP_binary = dec2bin(broadcastIP)
print('Broadcast IP:', broadcastIP, "->", broadcastIP_binary)
maxIP_binary = dec2bin(maxIP)
print('Max. IP:', maxIP, "->", maxIP_binary)
minIP = miniIP(networkID)
minIP_binary = dec2bin(networkID)
print('Min. IP:', minIP, "->", minIP_binary)