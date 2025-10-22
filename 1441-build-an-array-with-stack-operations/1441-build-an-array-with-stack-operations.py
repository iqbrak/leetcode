class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        results = []
        t_index = 0 

        for num in range(1, n + 1):
            if t_index >= len(target):
                break 
            
            if target[t_index] == num:
                results.append("Push")
                t_index += 1  
            else:
                results.append("Push")
                results.append("Pop")
        
        return results
