from math import sqrt
from collections import defaultdict

with open('файл1') as f:
    x, y = [int(x) for x in next(f).split()]
    r = int(next(f))

with open('файл2') as f:
    d = defaultdict(float)
    for line in f:
        key, value = line.split()
        d[float(key)] = (float(value))


for key in d:
    h = sqrt((key - x) ** 2 + (d[key] - y) ** 2)
    if h == r:
        print(0)
    elif h < r:
        print(1)
    else:
        print(2)
