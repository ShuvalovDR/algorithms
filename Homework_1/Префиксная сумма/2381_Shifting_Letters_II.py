from typing import List


class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        shift_indexes = [0 for _ in range(n)]
        for iteration in range(len(shifts)):
            start, end, direction = shifts[iteration]
            if direction == 1:
                shift_indexes[start] += 1
                if end + 1 < n:
                    shift_indexes[end + 1] -= 1
            else:
                shift_indexes[start] -= 1
                if end + 1 < n:
                    shift_indexes[end + 1] += 1
        prefix_sum = [0 for _ in range(n)]
        prefix_sum[0] = shift_indexes[0]
        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i - 1] + shift_indexes[i]
        answer = ['a' for i in range(n)]
        for i, letter in enumerate(s):
            asc_of_letter = ord(letter) - ord('a')
            asc_of_letter += prefix_sum[i]
            asc_of_letter = asc_of_letter % 26
            answer[i] = chr(asc_of_letter + ord('a'))
        return ''.join(answer)
sa = Solution()
sa.shiftingLetters(s = "abc", shifts = [[0,1,0],[1,2,1],[0,2,1]])