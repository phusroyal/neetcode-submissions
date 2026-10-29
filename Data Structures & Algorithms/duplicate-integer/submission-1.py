class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        answer_dict = {}
        for num in nums:
            if num not in answer_dict.keys():
                answer_dict[num] = 0
            else:
                return True
        return False

        