#!/usr/bin/env python3
import socket

HOST =  "www.google.com"
PORT = 80
BUFFER_SIZE = 1024

payload = """GET / HTTP/1.0
HOST: {HOST}

""".format(HOST = HOST)

def connect_socket(addr):
    (family, socketype, proto, cannoname, socketaddr) = addr
    try:
        s = socket.socket(family, socketype, proto)
        s.connect(socketaddr)
        s.sendall(payload.encode())
        full_data = b""
        while True:
            rep = s.recv(BUFFER_SIZE)
            if not rep:
                break
            full_data+=rep
        print(full_data)
        print("connected")
    except:
        print("retry")
        pass

def main():
    address = socket.getaddrinfo(HOST, PORT, proto = socket.SOL_TCP)
    addr = address[0]
    connect_socket(addr)
    socket.socket()
    
if __name__ == "__main__":
    main()




