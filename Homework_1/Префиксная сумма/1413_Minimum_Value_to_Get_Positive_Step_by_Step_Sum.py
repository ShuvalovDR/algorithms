from typing import List


class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        n = len(nums)
        prefix_sum = [0 for _ in range(n)]
        prefix_sum[0] = nums[0]
        min_value = nums[0]
        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i]
            if prefix_sum[i] < min_value:
                min_value = prefix_sum[i]
        if min_value < 0:
            answer = 1 - min_value
        else:
            answer = 1
        return answer
