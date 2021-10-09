class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 0
        while (len(nums)-1 > index):
            if nums[index+1] == nums[index]:
                nums.pop(index)
            else:
                index += 1
        
        return index+1