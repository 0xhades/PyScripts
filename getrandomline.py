import sys
import random

filepath = sys.argv[1]
l = sys.argv[2]
p = sys.argv[3]
m = sys.argv[4]
e = sys.argv[5]
count = 0
fh = open(filepath)
t = []
nums = []

def listContains(n, t, d):
    for i in n:
        if i - d == t:
            return True
    return False

for _ in range(int(l)): 
    n = random.randrange(int(p), int(m))
    nums.append(n)
nums.sort() 
while True:
    line = fh.readline()
    if listContains(nums, count, 1):
        if e not in line:
            t.append(line)
    count += 1
    if (not line) | (count == nums[-1] - 1):
        break

fh.close()

print('the lines:\n')
for n in t:
    print(n)
