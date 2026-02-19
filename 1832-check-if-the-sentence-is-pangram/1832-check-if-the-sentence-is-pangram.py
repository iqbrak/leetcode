class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabet = "abcdefghijklmnopqrstuvwxyz"

        for a in alphabet:
            if a not in sentence:
                return False

        return True

