from math import sqrt as msqrt
from random import random

def sqrt(x, eps):
    l = 0.
    r = max(1, float(x))
    while r - l > eps:
        m = (l + r) / 2
        if m ** 2 < x:
            l = m
        else:
            r = m
    return (l + r) / 2


eps = 1e-8
while True:
    x = random() * 100
    y1 = msqrt(x)
    y2 = sqrt(x, eps)
    if abs(y1 - y2) > eps:
        print(f'fail: {x:.9f}')
        exit(0)
    else:
        print('OK')
