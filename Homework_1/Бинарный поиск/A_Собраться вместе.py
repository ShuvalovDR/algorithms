def ok(t):
    global x, v, n
    lefts = [0] * n
    rights = [0] * n
    for i in range(n):
        lefts[i] = x[i] - v[i] * t
        rights[i] = x[i] + v[i] * t
    if min(rights) - max(lefts) >= 0:
        return True
    else:
        return False


n = int(input())
x = [0] * n
v = [0] * n
for i in range(n):
    x[i], v[i] = map(int, input().split())
left = 0
right = 1e10
epsilon = 1e-6
middle = 0
while abs(right - left) >= epsilon:
    middle = (left + right) / 2
    if ok(middle):
        right = middle
    else:
        left = middle
print(middle)
