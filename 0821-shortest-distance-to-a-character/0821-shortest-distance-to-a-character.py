class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        result = []

        indexes = [i for i, ch in enumerate(s) if ch == c]

        for i in range(n):
            temp = float("inf")
            for index in indexes:
                temp = min(temp, abs(i - index))
            result.append(temp)

        return result

