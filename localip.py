#!/usr/bin/env python3

##############################
# localip.py #
# ========== #
# Get own local IP address
# Copyright (c)2025 Ivaylo Vasilev. Released under the MIT License; see LICENSE for details.
# Author: Ivaylo Vasilev
##############################

import socket
import sys

# Create a socket and connect to Google's DNS public server at 8.8.8.8:53
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect(("8.8.8.8", 53))
except OSError as e:
    print(f"error: {e}")
    sys.exit(1)
except TimeoutError as e:
    print(f"error: {e}")
    sys.exit(2)
except InterruptedError as e:
    print(f"error: {e}")
    sys.exit(3)
except KeyboardInterrupt:
    print("aborted")
    sys.exit(4)

ip = s.getsockname()
print(f"[+] {ip[0]}")
