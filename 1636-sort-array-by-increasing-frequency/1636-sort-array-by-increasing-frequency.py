class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        n = len(nums)
        for i in range(n):
            for j in range(0, n - i - 1):
                if freq[nums[j]] > freq[nums[j + 1]]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                elif freq[nums[j]] == freq[nums[j + 1]] and nums[j] < nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]

        return nums
