class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0
        size = float('inf')
        sum = 0
        for j in range(len(nums)):
            sum += nums[j]
            while sum >= target:
                size = min(size,j-i+1)
                sum -= nums[i]
                i += 1            
        return 0 if size == float('inf') else size
            
            

        