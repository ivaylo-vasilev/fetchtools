# Fetch tools
Python based CLI programs for fetching system information, local or public IP, and more.
---

*I decided to create a collection of CLI programs for fetching information about the system, local network addresse, public IP adresse(s), and more using mainly the libraries that are coming by default with Python.*

---

## sysfetch.py
Fetch system information.

## localip.py
Get the local IP address.

## publicip.py
Get the public IP address. Supports both IPv4 and IPv6 addresses.

```
usage: publicip [-h] [-4] [-6] [-a] [--version]

Public IP

options:
  -h, --help  show this help message and exit
  -4, --ipv4  show IPv4
  -6, --ipv6  show IPv6
  -a, --all   show all IPs
  --version   show program version
```

## identify.py
Get the hostname of any device on the local network by its IP address.

