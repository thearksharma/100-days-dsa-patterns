from typing import List
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        maxCount = count = 0
        seen = {}
        for right in range(len(s)):
            if s[right] not in seen:
                seen[s[right]] = 1
            else:
                seen[s[right]] += 1

            while seen[s[right]] > 1:
                seen[s[left]] -= 1
                left += 1
            
            maxCount = max(right - left + 1,maxCount)
        return maxCount