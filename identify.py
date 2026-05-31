#!/usr/bin/env python3

##############################
# identify.py #
# =========== #
# Identify a machine (hostname) from local network
# Copyright (c)2025 Ivaylo Vasilev. Released under the MIT License; see LICENSE for details.
# Author: Ivaylo Vasilev
##############################

import socket
import argparse
import sys

parser = argparse.ArgumentParser(description="Identify a machine (hostname) from local network")
parser.add_argument("ip", nargs="?", help="enter local IP address")
args = parser.parse_args()

if len(sys.argv) == 1:
    parser.print_usage()
    sys.exit(1)

ip = args.ip

try:
    machine = socket.gethostbyaddr(ip)
    print(f"[+] {machine[0]}")
except socket.gaierror as e:
    print(f"error: {e}")
except socket.herror as e:
    print(f"error: {e}")
