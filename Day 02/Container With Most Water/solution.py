from typing import *
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        maxWater = 0
        while left <= right:
            width = right - left
            if height[left] <= height[right]:
                currWater = width*height[left]
                maxWater = max(currWater,maxWater)
                left += 1
            else:
                currWater = width * height[right]
                maxWater = max(currWater,maxWater)
                right -= 1
        return maxWater

