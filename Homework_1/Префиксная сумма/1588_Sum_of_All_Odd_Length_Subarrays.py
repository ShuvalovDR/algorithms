from typing import List


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:

        n = len(arr)
        prefix_sum = [0 for _ in range(n)]
        prefix_sum[0] = arr[0]
        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i - 1] + arr[i]
        if n % 2 == 0:
            max_step = n - 1
        else:
            max_step = n
        total = prefix_sum[n - 1]
        for step in range(2, max_step, 2):
            for i in range(n):
                if i + step < n:
                    total += prefix_sum[i + step]
                    if i - 1 >= 0:
                        total -= prefix_sum[i - 1]
                else:
                    break

        return total

