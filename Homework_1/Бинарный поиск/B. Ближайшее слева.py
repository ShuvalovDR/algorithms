n, k = map(int, input().split())
a = list(map(int, input().split()))
q = list(map(int, input().split()))
for x in q:
    left = 0
    right = n - 1
    ans = 0
    while left <= right:
        middle = (left + right) // 2
        if a[middle] <= x:
            left = middle + 1
            ans = middle
        else:
            right = middle - 1
    if x < a[0]:
        print(0)
    else:
        print(ans + 1)
