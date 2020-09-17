import string
import itertools
import sys


def generate_strings(length, chars):
    list = []
    for item in itertools.product(chars, repeat=length):
        list.append("".join(item) + '\n')
    return list

chars = str(sys.argv[1])
length = int(sys.argv[2])

f = open("list.txt", 'w')
f.writelines(generate_strings(length, chars))
f.close()
