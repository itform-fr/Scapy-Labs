import base64
from scapy.all import *

with open('fichier à créer', "wb") as f:
  while True:
      packet=sniff(filter="icmp[icmptype]==icmp-echo and ! icmp[8:4]==0x636f6b3f ",count=1)
      b64_payload = packet[0][Raw].load
      bytes_read = base64.b64decode(b64_payload)      
      if not bytes_read:
          break
      f.write(bytes_read)
