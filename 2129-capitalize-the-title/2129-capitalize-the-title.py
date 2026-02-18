class Solution:
    def capitalizeTitle(self, title: str) -> str:
        words = title.split()
        result = []

        for word in words:
            word = word.lower()
            if len(word) <= 2:
                result.append(word)
            else:
                first = word[0].upper()
                rest = ""
                for i in range(1, len(word)):
                    rest += word[i]
                
                result.append(first + rest)

        return " ".join(result)