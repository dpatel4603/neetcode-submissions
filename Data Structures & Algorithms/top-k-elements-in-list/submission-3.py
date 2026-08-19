from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counts = Counter(nums)
        top = sorted(counts.items(), key=lambda x: x[1], reverse=True)

        print(top[0])
        return [num for num, freq in top[:k]]