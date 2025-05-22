import socket

s = socket.socket()

try:
    s.connect(('localhost', 8000))
    while True:
        ip = input("Enter the website to ping (or 'exit' to quit): ")
        if ip.lower() == 'exit':
            break
        s.send(ip.encode())
        print("Server response:", s.recv(1024).decode())

except Exception as e:
    print(f"Error: {e}")

finally:
    s.close()
