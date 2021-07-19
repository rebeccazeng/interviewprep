class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = {}
        for i, num in enumerate(nums):
            comp = target - num
            if comp in values:
                return [values[comp], i]
            values[num] = i