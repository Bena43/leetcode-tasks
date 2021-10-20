class Solution:
    def mySqrt(self, x: int) -> int:
        root = 0
        while root*root <= x:
            root+=1
        return root-1