class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        pointer = 0
        end_of_list = len(nums)-1
        while pointer <= end_of_list:
            item = nums[pointer]
            if item == val:
                nums.pop(pointer)
                end_of_list -= 1
            else:
                pointer += 1
        return len(nums)
        