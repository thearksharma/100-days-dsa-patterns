from typing import List
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        seen = {}
        maxCount = 0
        i = 0
        for j in range(len(fruits)):
            seen[fruits[j]] = seen.get(fruits[j], 0) + 1
            while len(seen) > 2:
                seen[fruits[i]] -= 1
                if seen[fruits[i]] == 0 : del seen[fruits[i]]
                i += 1
            maxCount = max(maxCount,j-i+1)
        return maxCount