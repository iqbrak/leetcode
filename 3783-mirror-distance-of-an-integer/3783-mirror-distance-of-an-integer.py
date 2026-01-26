class Solution:
    def mirrorDistance(self, n: int) -> int:
        s = str(n)
        rev = ""

        for i in range(len(s) - 1, -1, -1):
            rev += s[i]

        return abs(n - int(rev))
