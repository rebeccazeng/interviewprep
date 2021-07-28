class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        rows = [None] * (numRows+1)
        # row1 = 1st row
        # create base cases
        rows[1] = [1]
        if numRows == 1:
            return [[1]]
        rows[2] = [1, 1]
        # create a new row
        for i in range(3, numRows+1):
            previous_row = rows[i-1]
            rows[i] = self.sumTwoNumbersSubarrays(previous_row)
        return rows[1:numRows+1]
    def sumTwoNumbersSubarrays(self, nums):
        sums = [1]
        for i in range(0, len(nums)-1):
            sums.append(nums[i] + nums[i+1])
        sums.append(1)
        return sums