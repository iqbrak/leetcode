class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        answer = []
        n = len(cost)
        minimum = cost[0]
        answer.append(minimum)

        for i in range(1, n):
            if minimum < cost[i]:
                answer.append(minimum)
            else:
                answer.append(cost[i])
                minimum = cost[i]

        return answer