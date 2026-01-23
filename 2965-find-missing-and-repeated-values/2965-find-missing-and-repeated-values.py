class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        repeated, miss = 0, 0
        max = n * n + 1
        list1d = sum(grid, [])

        for i in range(1, max):
            if list1d.count(i) > 1:
                repeated = i
            if list1d.count(i) == 0:
                miss = i
        
        return [repeated, miss]