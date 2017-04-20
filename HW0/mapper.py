#!/usr/bin/env python

import sys

def read_input(file):
    for line in file:
        yield line.split()


def main(separator='\t'):
    data = read_input(sys.stdin)
    for words in data:
        for word in words:
            if word[0].isalpha():
                print '%s%s%d' % (word[0].lower(), separator, 1)

if __name__ == "__main__":
    main()