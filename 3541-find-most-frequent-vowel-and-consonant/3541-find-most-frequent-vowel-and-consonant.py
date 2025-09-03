class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = "aiueo"
        vow_dict = {}
        con_dict = {}

        for i in s:
            if i in vowels:
                vow_dict[i] = vow_dict.get(i, 0) + 1
            else:
                con_dict[i] = con_dict.get(i, 0) + 1

        max_vow = max(vow_dict.values()) if vow_dict else 0
        max_con = max(con_dict.values()) if con_dict else 0

        return max_vow + max_con