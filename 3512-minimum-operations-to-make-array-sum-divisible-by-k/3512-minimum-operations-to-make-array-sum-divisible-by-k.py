class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        total = sum(nums)
        result = 0

        while total % k != 0:
            if total < k:
                result = total
                break
            else:
                result += 1
                total -= 1
        
        return result
            


