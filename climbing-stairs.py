class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n
        else:
            s1 = 1
            s2 = 2
            for i in range(3, n+1):
                step = s1 + s2
                s1 = s2
                s2 = step
        return s2
