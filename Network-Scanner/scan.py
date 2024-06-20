#!/usr/bin/python3
import sys
import argparse

from time import sleep
from scapy.all import *

parser = argparse.ArgumentParser(description="mon petit scanner de ports")
parser.add_argument('-a','--address', help='adresse ip à scanner',dest='ip',type=str)
parser.add_argument('-p','--port', help='port à scanner',dest='port',type=int)
parser.add_argument('-r','--range', help='étendue de port notée: 10000-15000',dest='range',type=str)
parser.add_argument('-o','--output', help='nom du fichier dans lequel écrire les résultats',dest='file',type=str)

args = parser.parse_args()
fichier=args.file
if not args.ip or not (args.port or args.range) or not args.file:
    parser.print_help()
    exit(1)
with open(fichier,'a') as file:
  file.write("host: " + args.ip + "\n")  
  if args.range:
      debut=int((args.range).split("-")[0])
      fin=int((args.range).split("-")[1])
      try:
        for i in range(debut,fin+1):
            packet=sr1(IP(dst=args.ip)/TCP(dport=i,flags="S"),timeout=0.05,verbose=0)
            if packet:
              value=packet[TCP].flags
              if value == "SA":
                print("\nle port " + str(i) + " est ouvert")
                file.write("port " + str(i) + " ouvert\n")
              else:
                  print(".", end="", flush=True)
            else:
                print(".", end="", flush=True)
      except KeyboardInterrupt:
        print("\nL'execution à été interrompue")
  else:
     packet=sr1(IP(dst=args.ip)/TCP(dport=args.port,flags="S"),verbose=0,timeout=2)
     value=packet[TCP].flags
     if value == "SA":
       print("\nle port " + str(args.port) + " est ouvert")
     else:
       print(".",end='')
  print("\n")

