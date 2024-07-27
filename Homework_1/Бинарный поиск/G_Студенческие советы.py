def ok(x):
    global a
    global k
    global n
    number = x * k
    for i in range(n):
        number -= min(a[i], x)
    if number <= 0:
        return True
    else:
        return False


k = int(input())
n = int(input())
a = [0 for _ in range(n)]
answer = 0
for i in range(n):
    a[i] = int(input())
ans = 1
l = 1
r = 10**14 + 1
while r >= l:
    middle = (l + r) // 2
    if ok(middle):
        l = middle + 1
        ans = middle
    else:
        r = middle - 1
print(ans)