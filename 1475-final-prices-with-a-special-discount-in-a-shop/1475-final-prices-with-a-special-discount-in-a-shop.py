class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        result = []

        for i in range(n):
            for j in range(i + 1, n):
                if prices[j] <= prices[i]:
                    result.append(prices[i] - prices[j])
                    break
            result.append(prices[i])

        return result 

