class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        result = []

        for ord in order:
            if ord in friends:
                result.append(ord)

        return result