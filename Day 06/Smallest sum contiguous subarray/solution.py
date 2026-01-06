from typing import List
class Solution:
    def smallestSumSubarray(self, A, N):
        ans = bestEnding = A[0]
        for num in A[1::]:
            bestEnding = min(num, num + bestEnding)
            ans = min(ans, bestEnding)
        return ans