import sys
import random

n = 0
l = len(sys.argv)
fn = sys.argv[1]
if l > 2:
    n = int(sys.argv[2])

f = open(fn, 'r')
lines = f.readlines()

if n != 0:
    inx = []
    i = len(lines) / n
    r = len(lines)
    for x in range(n):
        if x == 0:
            inx.append(r)
            continue
        inx.append(r - i)
        r = r - i

    lists = []
    for x in reversed(inx):
        if x != 0:
            h = x - i
            list = []
            while h < x:
                list.append(lines[h])
                h += 1
            lists.append(list)

    final = []
    for i in range(len(lists[0])):
        for x in lists:
            final.append(x[i])

else:
    final = []
    inx = []
    ind = []
    for i in range(len(lines)):
        inx.append(i)
    for i in reversed(inx):
        ind.append(i)
    xni = random.sample(ind, len(ind))
    for i in xni:
        final.append(lines[i])

f = open(fn, 'w')
f.writelines(final)
f.close()
