import socket

HOST = "192.168.1.9"  # IP address of the PLC
PORT = 50505  # Arbitrary port I used in the Ladder Logic program

with socket.socket() as s:
    s.connect((HOST, PORT))
    s.sendall(b'REQ')
    print(s.recv(1024))
