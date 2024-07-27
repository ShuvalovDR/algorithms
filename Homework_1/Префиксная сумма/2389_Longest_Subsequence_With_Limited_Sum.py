from typing import List


class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        k = len(queries)
        prefix_sum = [0 for _ in range(n)]
        prefix_sum[0] = nums[0]
        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i]
        answer = [0 for _ in range(k)]
        for i, x in enumerate(queries):
            left = 0
            right = n - 1
            ans = 0
            while left <= right:
                middle = (left + right) // 2
                if prefix_sum[middle] <= x:
                    left = middle + 1
                    ans = middle
                else:
                    right = middle - 1
            if prefix_sum[0] > x:
                answer[i] = 0
            else:
                answer[i] = ans + 1
        return answer
