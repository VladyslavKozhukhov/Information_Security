import assemble
def patch_program(path):
    with open(path, 'rb') as reader:
        data = reader.read()
    Ldata = list(data)
    patch1 = assemble.assemble_file("patch1.asm")
    patch2 = assemble.assemble_file("patch2.asm")
    for i in range(len(patch1)):
        Ldata[0x633+i] = patch1[i]
    for j in range(len(patch2)):
        Ldata[0x5d0+j] = patch2[j]
    data = "".join(Ldata)
    with open(path + '.patched', 'wb') as writer:
        writer.write(data)


def main(argv):
    if len(argv) != 2:
        print('USAGE: python {} <readfile-program>'.format(argv[0]))
        return -1
    path = argv[1]
    patch_program(path)
    print('done')


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
