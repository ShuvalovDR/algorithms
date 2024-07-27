def ok(t: str, p: str, index: int) -> bool:
    global a
    global n
    if len(p) > len(t):
        return False
    answer = []
    is_in_t = [1 for i in range(n)]
    for i in range(index):
        is_in_t[a[i]] = 0
    for i, letter in enumerate(range(n)):
        if is_in_t[i] == 1:
            answer.append(t[i])

    t = ''.join(answer)
    p = list(p)
    p.reverse()
    for letter in t:
        if len(p) == 0:
            return True
        l = p.pop()
        if letter == l:
            continue
        else:
            p.append(l)
    if len(p) == 0:
        return True
    else:
        return False


t = input()
p = input()
a = list(map(lambda x: int(x) - 1, input().split()))
n = len(a)
left = 0
right = n - 1
while right >= left:
    middle = (left + right) // 2
    if ok(t, p, middle):
        left = middle + 1
    else:
        right = middle - 1
print(left - 1)
