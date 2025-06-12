#!/usr/bin/env python3

import platform
import shutil
import getpass
import socket
from urllib import request, error
import argparse
import sys

# Fetch system information using the default Python libraries

parser = argparse.ArgumentParser(prog="sysfetch", description="System information fetch", epilog="(c)Ivaylo Vasilev")
parser.add_argument("--version", action="version", version="%(prog)s 0.5.1", help="show program version")
args = parser.parse_args()


def main():
    information = systemfetch()
    print(information)


def systemfetch():
    sysinfo = platform.uname()
    username = getpass.getuser()
    localip = local_ip()
    publicip = public_ip()

    terminal_size = shutil.get_terminal_size()
    columns = terminal_size[0]
    lines = terminal_size[1]

    return f"""
    System Information
    ==================

    System        : {sysinfo[0]}
    Release       : {sysinfo[2]}
    Version       : {sysinfo[3]}

    Machine       : {sysinfo[4]}
    Hostname      : {sysinfo[1]}
    Local IP      : {localip}
    Public IPv4   : {publicip[0]}
    Public IPv6   : {publicip[1]}

    Username      : {username}
    Terminal size : {columns} x {lines}

    """


def local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect(("8.8.8.8", 53))
    except OSError:
        return "Network is unreachable"
    except TimeoutError:
        return "Connection time out"
    except InterruptedError:
        return "Interrupted"

    ip = s.getsockname()
    
    return ip[0]


def public_ip():
    try:
        u4 = request.urlopen("https://ipv4.icanhazip.com")
        publicipv4 = u4.read()
        u6 = request.urlopen("https://ipv6.icanhazip.com")
        publicipv6 = u6.read()
        u4.close()
        u6.close()
        return (publicipv4.decode().strip(), publicipv6.decode().strip())
    except error.URLError:
        return ("None", "None")


if __name__ == "__main__":
    main()
