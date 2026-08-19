class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # 1. Sort the numbers and keep it sorted
        sorted_nums = sorted(nums)

        longest = 1
        current_streak = 1

        for i in range(len(sorted_nums) - 1):
            # Skip duplicates (e.g., [1, 2, 2, 3])
            if sorted_nums[i] == sorted_nums[i + 1]:
                continue

            # Check if next number is consecutive
            if sorted_nums[i] + 1 == sorted_nums[i + 1]:
                current_streak += 1
            else:
                # Streak broken! Update longest and reset
                longest = max(longest, current_streak)
                current_streak = 1

        return max(longest, current_streak)
