class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        combined = []
        for i in range(len(names)):
            combined.append([heights[i], names[i]])
        
        combined.sort(reverse=True)
        
        result = []
        for item in combined:
            result.append(item[1])
        
        return result