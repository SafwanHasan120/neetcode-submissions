class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        for point in points:
            dist = pow(pow(point[0], 2) + pow(point[1], 2), 0.5)
            heapq.heappush(h, (dist, point))
        print(h)
        res = []
        count = 0
        while count < k:
            dist, point = heapq.heappop(h)
            res.append(point)
            count += 1
        return res