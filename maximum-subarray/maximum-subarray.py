class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if (len(nums) == 0):
            return 0
        maxSum = nums[0]
        currentSum = nums[0]
        # [-2,1,-3,4,-1,2,1,-5,4]
        for i in range(1, len(nums)):
            n = nums[i]
            currentSum = max(currentSum + n, n)
            # is this number + past currentSum better or worse than just having the number on its own?
            maxSum = max(maxSum, currentSum)
            # is the currentSum better than the past maxSum that we got?
        return maxSum
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        if (len(nums) == 0):
            return 0
        maxSum = nums[0]
        currentSum = nums[0]
        for i in range(1, len(nums)):
            n = nums[i]
            currentSum = max(currentSum + n, n)
            maxSum = max(maxSum, currentSum)
        return maxSum