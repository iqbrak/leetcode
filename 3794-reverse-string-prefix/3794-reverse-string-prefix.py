class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        n = k - 1
        result = ""

        for i in range(n, 0, -1):
            result += s[i]

        for i in range(k, len(s)):
            result += s[i]
        
        return result

        