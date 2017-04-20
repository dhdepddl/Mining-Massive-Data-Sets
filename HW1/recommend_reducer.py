#!/usr/bin/env python

from itertools import groupby
from operator import itemgetter
import sys



def read_mapper_output(file, separator='\t'):
    for line in file:
        yield line.rstrip().split(separator)


def main(separator='\t'):
    data = read_mapper_output(sys.stdin, separator=separator)
    for user_pair, value in groupby(data, itemgetter(0)):
        try:
            total_count = sum(int(count) if count != '0' else ValueError for user_pair, count in value)
            print '%s%s%s' % (user_pair, separator, total_count)

        except TypeError:
            pass

        except ValueError:
            pass


if __name__ == "__main__":
    main()