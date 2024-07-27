def ok(x):
    global have_ingredients, requirements, cost, r
    n = len(have_ingredients)
    requirements_for_x = [0 for i in range(n)]
    for i in range(n):
        requirements_for_x[i] = max(0, (x * requirements[i] - have_ingredients[i]) * cost[i])
    if r - sum(requirements_for_x) >= 0:
        return True
    else:
        return False


receipt = input()
have_ingredients = list(map(int, input().split()))
cost = list(map(int, input().split()))
r = int(input())
requirements = [0, 0, 0]
for letter in receipt:
    if letter == 'B':
        requirements[0] += 1
    elif letter == 'S':
        requirements[1] += 1
    else:
        requirements[2] += 1
ans = 0
left = 0
right = 10**14
while left <= right:
    middle = (left + right) // 2
    if ok(middle):
        left = middle + 1
        ans = middle
    else:
        right = middle - 1
print(ans)
