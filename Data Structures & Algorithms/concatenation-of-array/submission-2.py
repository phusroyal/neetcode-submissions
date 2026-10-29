class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums_len = len(nums)
        for i in range(nums_len):
            nums.append(nums[i])
        
        return nums
