class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        [6, 0, 5, 0, 4]
        [3, 3, 3, 3, 3]
        [3, -3, 2, -3, 1]
        [3, 0, 2, -1, 0]

        [1, 2, 3, 4]
        [2, 2, 4, 1]
        [-1, 0, -1, 3]
        [-1, 0, -2, 1]


        curSum = 0
        for i in range(len(gas)):
            curSum += (gas[i] - cost[i])
        
        if curSum < 0:
            return -1
        
        total = 0
        res = 0
        for i in range(len(gas)):
            total += (gas[i] - cost[i])
            if total < 0:
                total = 0
                res = i + 1

        return res