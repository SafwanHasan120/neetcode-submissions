class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = []
        for stone in stones:
            heapq.heappush(h, -stone)
        
        while len(h) > 1:
            x = heapq.heappop(h) * -1
            y = heapq.heappop(h) * -1
            if x != y:
                heapq.heappush(h, -(abs(y-x)))
            
        if len(h) == 1:
            return h[0] * -1
        else:
            return 0