class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        result = 0

        for i in range(len(s)):
            curr_num = dict[s[i]]

            if i + 1 < len(s):
                next_num = dict[s[i+1]]
                if curr_num < next_num:
                    result -= curr_num
                else:
                    result += curr_num 
            else:
                result += curr_num        
                  
        return result

        


        