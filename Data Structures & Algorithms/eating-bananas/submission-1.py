class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxR = max(piles)
        lo, hi = 1, maxR
        while lo < hi:
            #1, 2, 3, 4, 5, 6
            mid = (lo + hi) // 2
            hoursNeeded = 0
            for i in range(len(piles)):
                hoursNeeded += -(-piles[i] // mid)
            if(hoursNeeded <= h):
                hi = mid
            else:
                lo = mid + 1
        return lo