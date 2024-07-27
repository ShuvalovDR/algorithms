from typing import List


class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        n = len(hours)
        prefix_sum = [0 for i in range(n)]
        if hours[0] > 8:
            prefix_sum[0] = 1
        else:
            prefix_sum[0] = -1
        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i - 1]
            if hours[i] > 8:
                prefix_sum[i] += 1
            else:
                prefix_sum[i] -= 1
        answer = 0
        first_entrance = {}
        for i in range(n):
            if prefix_sum[i] > 0:
                answer = i + 1
            else:
                if prefix_sum[i] - 1 in first_entrance:
                    answer = max(answer, i - first_entrance[prefix_sum[i] - 1])
                if prefix_sum[i] not in first_entrance:
                    first_entrance[prefix_sum[i]] = i

        return answer
an = Solution().longestWPI([9, 6, 0, 8, 9, 9])
print(an)


