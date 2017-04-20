#!/usr/bin/env python

from itertools import groupby
from operator import itemgetter
import sys

current_count = 0


def read_mapper_output(file, separator='\t'):
    for line in file:
        yield line.rstrip().split(separator)


def main():
    data = read_mapper_output(sys.stdin)
    for user, friend_rel in groupby(data, itemgetter(0)):
        try:
            friend_list = map(itemgetter(1), friend_rel)
            friend_list = [[int(val) for val in x.split(',')] for x in friend_list]
            friend_list.sort()
            friend_list.reverse()
            friend_list = [str(x[1]) for x in friend_list]
            if len(friend_list) >= 10:
                friend_list = friend_list[:10]
            print "%s%s%s" % (user, ' ', ','.join(friend_list))
        except ValueError:
            pass


if __name__ == "__main__":
    main()