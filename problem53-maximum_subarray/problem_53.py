class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current = result = nums[0]
        for i in range(1, len(nums)):
            if current > 0:
                # Is it better to start fresh, or add previous value?
                current += nums[i]
            else:
                current = nums[i]
                
            # Is the above result, best result until now?
            if current > result:
                result = current
        return result