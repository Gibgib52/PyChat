"""
    Chat over the network using sockets.
"""

import socket
import ANSIescs as ansi

c = ansi.c

Host = "127.0.0.1"
Port = 65522

# our hostname
local_hostname = socket.gethostname()
# full qualified hostname
local_fqdn = socket.getfqdn()
# our ip
ip_address = socket.gethostbyname(local_hostname)

def format_fqdn(fqdn):
    split_fqdn = fqdn.split(".")
    formatted_fqdn = split_fqdn(".")[0]

formatted_fqdn = format_fqdn(local_fqdn)

print(f"{c.GREEN}{'hostname:':<10} {local_hostname:>25}{c.ENDC}\n"\
      f"{'fqdn:':<10} {local_fqdn:>25}\n"\
      f"{'ip:':<10} {ip_address:>25}")

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# with statement automatically closes socket
with sock as s:
    s.bind((Host, Port))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected to {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)