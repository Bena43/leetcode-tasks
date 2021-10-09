class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0
        while len(nums) > index:
            if val == nums[index]:
                nums.pop(index)
            else:
                index += 1
        
        return index+1