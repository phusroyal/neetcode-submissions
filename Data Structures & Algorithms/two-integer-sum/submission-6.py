class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, val in enumerate(nums):
            diff = target - val
            if diff in seen:
                # Pair found: seen[diff] was visited earlier
                return [seen[diff], i]
            seen[val] = i