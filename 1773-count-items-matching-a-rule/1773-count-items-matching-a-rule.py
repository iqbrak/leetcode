class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        n = len(items)
        ruleKeys = ["type", "color", "name"]
        keyIdx = ruleKeys.index(ruleKey)
        result = 0

        for i in range(n):
            if items[i][keyIdx] == ruleValue:
                result += 1

        return result