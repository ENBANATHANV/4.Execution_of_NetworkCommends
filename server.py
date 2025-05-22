import socket
from pythonping import ping

# Create a TCP socket
s = socket.socket()
s.bind(('localhost', 8000))
s.listen(1)

print("Server is listening on port 8000...")

# Accept client connection
c, addr = s.accept()
print(f"Connected to {addr}")

while True:
    hostname = c.recv(1024).decode().strip()
    if not hostname:
        break
    print(f"Pinging: {hostname}")
    try:
        result = ping(hostname, count=1, verbose=False)
        c.send(str(result).encode())
    except Exception as e:
        c.send(f"Ping failed: {e}".encode())

c.close()
