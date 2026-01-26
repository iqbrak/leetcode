class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        key_dict = {}
        idx = 0

        for i in key:
            if i != " " and i not in key_dict:
                key_dict[i] = alphabet[idx]
                idx += 1

        result = ""
        for i in message:
            if i == " ":
                result += " "
            else:
                result += key_dict[i]

        return result
