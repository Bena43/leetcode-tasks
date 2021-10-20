class Solution:
    def __init__(self):
        self.saved_solutions = [0,1,2]
    def climbStairs(self, n: int) -> int:
        try:
            self.saved_solutions[n]
        except:
            self.saved_solutions.append(self.climbStairs(n - 1) + self.climbStairs(n - 2))
        return self.saved_solutions[n]
        