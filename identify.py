#!/usr/bin/env python3

import socket
import argparse
import sys

parser = argparse.ArgumentParser(description="Identify a machine from local network")
parser.add_argument("ip", nargs="?", help="enter local IP address")
args = parser.parse_args()

if len(sys.argv) == 1:
    parser.print_usage()
    sys.exit(1)

ip = args.ip

try:
    machine = socket.gethostbyaddr(ip)
    print(machine[0])
except socket.gaierror as e:
    print(f"error: {e}")
except socket.herror as e:
    print(f"error: {e}")
