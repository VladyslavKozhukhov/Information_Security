def fix_message(path):
    with open(path, 'rb') as reader:
        data = reader.read()
    num = 0x0ae
    data+=('\x00'*0x100)
    first = data[0]

    i=2
    while i<ord(first)+2:
        exp = ord(data[i])
        num = num ^(exp)
        i = i + 1
    Ldata = list(data)
    Ldata[1] = chr(num)
    data= "".join(Ldata)
       
    with open(path + '.fixed', 'wb') as writer:
        writer.write(data)


def main(argv):
    if len(argv) != 2:
        print('USAGE: python {} <msg-file>'.format(argv[0]))
        return -1
    path = argv[1]
    fix_message(path)
    print('done')


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
