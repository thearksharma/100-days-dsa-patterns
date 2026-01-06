from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxEnding = minEnding = ans = nums[0]

        for num in nums[1:]:
            prevMax = maxEnding
            prevMin = minEnding

            maxEnding = max(num, num * prevMax, num * prevMin)
            minEnding = min(num, num * prevMax, num * prevMin)

            ans = max(ans, maxEnding)

        return ans
