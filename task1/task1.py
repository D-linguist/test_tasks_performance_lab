import argparse
from itertools import cycle

parser = argparse.ArgumentParser()
parser.add_argument("--n", type=int, default=1)
parser.add_argument("--m", type=int, default=1)
args = parser.parse_args()
n, m = args.n, args.m

lm = []
u = 1
for i in range(n):
    lm.append(u)
    u += 1

cyc_lm = cycle(lm)

lst = []
for i in range(n * m):
    lst.append(next(cyc_lm))

x = 0
outlst = []
while True:
    lsta = lst[x:x+m]
    outlst.append(lsta[0])
    # print(lsta)
    if lsta[m-1] == 1:
        break
    x += m - 1

for i in range(len(outlst)):
    print(outlst[i], end='')
