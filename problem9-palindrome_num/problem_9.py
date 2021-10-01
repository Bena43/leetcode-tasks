class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0:
            # Negative numbers cannot be palindrome according to question definition
            return False
        # Map digits as string chars, in to integer list 
        digit_list = list(map(int,str(x)))
        
        # Divided by two to get better runtime. difference between 60ms and about 100ms
        for i in range(int(len(digit_list)/2)):
            if digit_list[i] != digit_list[-1-i]:
                # Run on list from left to right, compare with mirrored digit from right to left.
                # If not equal, not a Palindrome.
                return False
            
        return True
        