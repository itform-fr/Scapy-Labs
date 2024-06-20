#!/usr/bin/python3
import base64
from scapy.all import *
while True:
  packet=sniff(filter="icmp[icmptype]==icmp-echo and icmp[8:4]==0x54445131 and icmp[12:2]==0x4d31",count=1)

  message=packet[0][Raw].load
  message=message.decode('utf-8')
  message=base64.b64decode(message)
  message=message.decode('utf-8')
  message=message.split('--')[1]
  print('\033[32m' + message + '\033[0m')
  print('\033[36m' + "à nous: " + '\033[0m',end='',flush=True)
  userinput=input()
  userinput="L453R--" + userinput
  userinput=userinput.encode('utf-8')
  b64_bytes = base64.b64encode(userinput)
  b64_message = b64_bytes.decode('utf-8')
  resp=packet[0]
  resp=(Ether(src=packet[0][Ether].dst,dst=packet[0][Ether].src)/IP(dst=packet[0][IP].src,src=packet[0][IP].dst)/ICMP(type=0)/Raw(str(b64_message)))
  sendp(resp,verbose=0)
