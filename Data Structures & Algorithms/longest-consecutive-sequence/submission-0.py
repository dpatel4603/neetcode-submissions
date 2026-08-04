class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        num_set = set(nums)
        longest = 0

        for num in num_set:
            if num - 1 in num_set:
                continue
            
            length = 1
            cur = num 
            while cur + 1 in num_set: 
                cur += 1
                length += 1

            
            longest = max(longest, length)
        
        return longest