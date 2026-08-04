class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {}
        # {num : index(i)}

        for i, num in enumerate(nums):
            goal = target - num

            if goal in seen: 
                return [seen[goal], i]
            
            seen[num] = i
        
        return []

