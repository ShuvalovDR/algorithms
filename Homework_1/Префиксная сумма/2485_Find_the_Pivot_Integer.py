class Solution:
    def pivotInteger(self, n: int) -> int:
        a = [i for i in range(1, n + 1)]
        prefix_sum = [0 for _ in range(n)]
        suffix_sum = [0 for _ in range(n)]
        prefix_sum[0] = a[0]
        suffix_sum[n - 1] = a[n - 1]
        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i - 1] + a[i]
        for i in range(n - 2, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + a[i]
        for i in range(n):
            if prefix_sum[i] == suffix_sum[i]:
                return i + 1
        return -1

s = Solution()
print(s.pivotInteger(4))


