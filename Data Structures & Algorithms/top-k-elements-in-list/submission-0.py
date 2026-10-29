from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = Counter(nums)
        nums_dict_sorted = {k: v for k, v in sorted(
                                nums_dict.items(), 
                                key = lambda item: item[1], 
                                reverse=True)}
        
        return list(nums_dict_sorted.keys())[:k]
