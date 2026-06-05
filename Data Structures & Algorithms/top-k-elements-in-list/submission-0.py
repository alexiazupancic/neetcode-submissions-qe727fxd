class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        counted = Counter(nums)
        return [num for num, count in counted.most_common(k)]
        