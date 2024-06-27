#!/usr/bin/python3

from scapy.all import *
import base64

file=sniff(filter='icmp[icmptype]=icmp-echo and icmp[8:4]=0x526a4673',count=1)
file=file[0][Raw].load
file=base64.b64decode(file.decode()).decode().split(":")[1]
paquet=sniff(filter='icmp[icmptype]=icmp-echo and icmp[8:4]=0x526a4673',stop_filter=lambda p: p.haslayer(Padding))
fichier=open(file,'ab')
for i in range (0,len(paquet)-1):
  octets=paquet[i][Raw].load
  octets=octets.decode().split("=",1)[1]
  test=base64.b64decode(octets)
  fichier.write(test)
