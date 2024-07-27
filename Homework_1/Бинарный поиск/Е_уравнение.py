import math


def function(x: float, a: float) -> float:
    return x ** 2 + math.sqrt(x) - a


c = float(input())
left = 0
right = 1e5
middle = (left + right) / 2
epsilon = 1e-6
while abs(right - left) > epsilon:
    middle = (left + right) / 2
    if function(middle, c) * function(left, c) <= 0:
        right = middle
    else:
        left = middle
print(middle)
