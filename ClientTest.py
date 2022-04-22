import socket

Host = "127.0.0.1"
Port = 65522


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((Host, Port))
    s.sendall(b"Sockets! nice") # b for bytes
    data = s.recv(1024)

print(f"Received {data}")