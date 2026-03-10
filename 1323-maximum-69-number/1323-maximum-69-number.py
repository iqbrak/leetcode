class Solution:
    def maximum69Number (self, num: int) -> int:
        s = list(str(num))
        result = num

        for i in range(len(s)):
            temp = s.copy()

            if temp[i] == "6":
                temp[i] = "9"
            else:
                temp[i] = "6"

            new_num = int("".join(temp))

            if new_num > result:
                result = new_num

        return result