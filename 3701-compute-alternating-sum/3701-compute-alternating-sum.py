class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        n = len(nums)
        result = 0

        for i in range(n):
            if i % 2 == 0:
                result += nums[i]
            else:
                result -= nums[i]
        
        return result
