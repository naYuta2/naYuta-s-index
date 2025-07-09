import matplotlib.pyplot as plt
import math

def func(x):
    return 1.25 * math.sin(0.4 * x) * math.sin(0.6 * x) - x * math.sin(x)

x1 = 2.6
x2 = 2.9
n = 0
a = None
losses = []

while True:
    n+=1
    a = (x1*func(x2) - x2*func(x1)) / (func(x2) - func(x1))
    losses.append(func(a))

    if func(a) == 0 or abs(func(a)) < 10e-10:
        print("break!")
        break

    if func(a) > 0:
        x1 = a
    else:
        x2 = a
print(a, func(a), n)