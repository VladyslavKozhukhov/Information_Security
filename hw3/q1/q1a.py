def check_message(path):
    num = 0x0ae
    newFile = open(path,'r')
    text = newFile.read()
    first = text[0]
    second = text [1]
    text+=('\x00'*0x100)
    i=2
    while i<ord(first)+2:
        exp = ord(text[i])
        num = num ^(exp)
        i = i + 1
    if(num==ord(second)):
        return 1
    return 0


def main(argv):
    if len(argv) != 2:
        print('USAGE: python {} <msg-file>'.format(argv[0]))
        return -1
    path = argv[1]
    if check_message(path):
        print('valid message')
        return 0
    else:
        print('invalid message')
        return 1


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
