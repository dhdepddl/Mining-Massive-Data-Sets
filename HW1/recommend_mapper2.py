#!/usr/bin/env python

import sys


def read_input(file, separator=','):
    for line in file:
        yield line.rstrip().split(separator)


def main(separator=','):
    data = read_input(sys.stdin, separator=separator)
    for words in data:
        try:
            user = words[0]
            value = words[1].split('\t')
            if int(value[1]) != 0:
                print '%s%s%s%s%s' % (user, '\t', value[1], ',', value[0])

        except ValueError:
            pass


if __name__ == "__main__":
    main()