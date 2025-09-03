class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        vowels = "aiueo"
        result = 0

        for i, w in enumerate(words): 
            if i >= left and i <= right:
                if len(w) > 1:
                    if w[0] in vowels and w[-1] in vowels:
                        result += 1
                else: 
                    if w in vowels: 
                        result += 1
        
        return result

    