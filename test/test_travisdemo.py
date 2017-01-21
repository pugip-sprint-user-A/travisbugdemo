#! /usr/bin/env python

def test_func():
    return 0


def main(args):
    def usage():
        print 'usage: "%s" [-h]'%(args[0])
    if len(args)==2:
        if args[1]=='-h':
            usage()
            exit()
        else:
            usage()
    else:
        return test_func()

if __name__=='__main__':
    import sys
    sys.exit(main(sys.argv))

