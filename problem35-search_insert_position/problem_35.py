class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lower_bound = 0
        higher_bound = len(nums) - 1
        while higher_bound >= lower_bound:
            middle = (higher_bound + lower_bound) // 2
            if target == nums[middle]:
                return middle
            elif target > nums[middle]:
                lower_bound = middle + 1
            elif target < nums[middle]:
                higher_bound = middle - 1
        if lower_bound == len(nums):
            return len(nums)
        elif higher_bound < 0:
            return 0
        else:
            return lower_bound
