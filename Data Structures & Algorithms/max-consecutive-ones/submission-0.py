class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        counter = 0
        for v in nums:
            if v == 1:
                counter +=1 
            else:
                res = max(res, counter)
                counter = 0
        res = max(res, counter)
        return res