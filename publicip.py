#!/usr/bin/env python3

import argparse
from urllib import request, error

parser = argparse.ArgumentParser(prog="publicip", description="Public IP")
parser.add_argument("-4", "--ipv4", action="store_true", help="show IPv4")
parser.add_argument("-6", "--ipv6", action="store_true", help="show IPv6")
parser.add_argument("-a", "--all", action="store_true", help="show all IPs")
parser.add_argument("--version", action="version", version="%(prog)s 1.5", help="show program version")
args = parser.parse_args()

try:
    if args.ipv4:
        u = request.urlopen("https://ipv4.icanhazip.com")
        publicipv4 = u.read()
        print(f"Public IPv4 address: {publicipv4.decode().strip()}")
        u.close()
    elif args.ipv6:
        u = request.urlopen("https://ipv6.icanhazip.com")
        publicipv6 = u.read()
        print(f"Public IPv6: {publicipv6.decode().strip()}")
        u.close()
    elif args.all:
        u4 = request.urlopen("https://ipv4.icanhazip.com")
        publicipv4 = u4.read()
        u6 = request.urlopen("https://ipv6.icanhazip.com")
        publicipv6 = u6.read()
        print(f"Public IPv4: {publicipv4.decode().strip()}")
        print(f"Public IPv6: {publicipv6.decode().strip()}")
        u4.close()
        u6.close()
    else:
        u = request.urlopen("https://icanhazip.com")
        publicip = u.read()
        print(f"Public IP address: {publicip.decode().strip()}")
        u.close()
except error.URLError:
    print("error: could not fetch the public IP address")
