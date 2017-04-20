#!/usr/bin/env python

import sys

def read_input(file, separator = '\t'):
    for line in file:
        yield line.split()


def main(separator='\t'):
    data = read_input(sys.stdin)
    for words in data:
        try:
            user = words[0]
            if len(words) == 2:
                friends = words[1].split(',')
                for friend in friends:
                    for other in friends:
                        if friend == other:
                            continue
                        else:
                            print '%s%s%s%s%d' % (friend, ',', other, separator, 1)
                    print '%s%s%s%s%d' % (user, ',', friend, separator, 0)
        except ValueError:
            pass

if __name__ == "__main__":
    main()