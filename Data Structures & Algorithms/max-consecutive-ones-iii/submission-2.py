class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        count = 0
        curMax = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                count += 1
            while count > k:
                if nums[l] == 0:
                    count -= 1
                l += 1
            curMax = max(curMax, r - l + 1)
        return curMax