class Solution:
    def reverseDegree(self, s: str) -> int:
        result = 0
        i = 1

        for ch in s:
            res = 26 - (ord(ch) - ord('a'))
            result += (res * i)
            i += 1
            
        return result
