class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       # O(n), hashmap
        dict = {}
        for index, num in enumerate(nums):
            # Get the complimentery number for the current number (the difference between target and current number)
            diff_to_target = target - num
            # Search it in the dict. 
            if diff_to_target in dict:
                # If it existed - we found it! hashmap runtime is O(1)
                return [dict[diff_to_target], index]
            else:
                # No luck this iteration. adding current number to the dict. else is optional, here for readability.
                dict[num] = index
        
        # O(n^2)
        # for i, num1 in enumerate(nums):
        #     for j, num2 in enumerate(nums):
        #         if num1+num2 == target:
        #             return [i,j]
