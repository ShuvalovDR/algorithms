from typing import List


class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n = len(arr)
        k = len(queries)
        answer = [0 for i in range(k)]
        prefix_xor = [0 for i in range(n)]
        prefix_xor[0] = arr[0]
        for i in range(1, n):
            prefix_xor[i] = prefix_xor[i - 1] ^ arr[i]
        for i in range(k):
            left, right = queries[i]
            if left == 0:
                answer[i] = prefix_xor[right]
            else:
                answer[i] = prefix_xor[right] ^ prefix_xor[left - 1]
        return answer
