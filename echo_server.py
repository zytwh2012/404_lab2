#!/usr/bin/env python3

import socket

HOST =  ""
PORT = 8001
BUFFER_SIZE = 1024

def main():
    #create socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(1)
        conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(BUFFER_SIZE)
            if not data: break
            conn.sendall(data)

if __name__ == "__main__":
    main()
