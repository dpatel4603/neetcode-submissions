class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        num_set = set(nums)
        longest = 0

        for num in num_set:
            if num - 1 in num_set:
                continue
            
            cur = num + 1
            while cur in num_set: 
                cur += 1

            if cur - num > longest:
                longest = cur - num
            
        
        return longest