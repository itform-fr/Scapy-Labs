#!/bin/python3
from scapy.all import sniff,rdpcap
from scapy.contrib.cdp import *

#capture=sniff(filter="ether[20:2] == 0x2000",count=1,iface="ens3")
capture=rdpcap('/home/julien/capture.pcapng')
equipement=str(capture[0][CDPv2_HDR].msg[5].cap)
nom=capture[0][CDPv2_HDR].msg[0].val.decode()
ip=capture[0][CDPv2_HDR].msg[3].addr[0].addr
iface=capture[0][CDPv2_HDR].msg[4].iface.decode()
print("")
match equipement:
    case equipement if "Switch" in equipement and "Router" in equipement:
        print("L'équipement sur lequel nous sommes connectés est un switch L3 nommé " + nom)
    case equipement if "Switch" in equipement:
        print("L'équipement sur lequel nous sommes connectés est un switch L2 nommé " + nom)
    case equipement if "Router" in equipement:
        print("L'équipement sur lequel nous sommes connectés est un routeur nommé " + nom)
    case equipement if "Bit25" in equipement:
        print("L'équipement sur lequel nous sommes connectés est un Téléphone nommé "  + nom)
print("\n---------------------------------------------------\n")
print("Adresse IP:      " + ip )
print("Interface:       " + iface )
try:
    vlan=capture[0][CDPv2_HDR].msg[8].vlan
    print("Vlan:            " + str(vlan))
except:
    print("pas de vlans")

try:
    networks= capture[0][CDPv2_HDR].msg[6].prefixes
    for i in range (0,len(networks)):
        print("Réseau :         " + networks[i].prefix + "/" + str(networks[i].plen))
except:
    print("pas de préfixes")
