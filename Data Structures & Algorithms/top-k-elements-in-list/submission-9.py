class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        res = []
        counts = Counter(nums)

        top = sorted(counts.items(), key=lambda x: x[1], reverse=True)

        for num, freq in top[:k]:
            res.append(num)


        return res