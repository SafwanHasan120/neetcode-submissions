class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = 0
        curMin, curMax = 1, 1
        if(len(nums) == 1):
            return nums[0]
        for num in nums:
            temp = curMax * num
            curMax = max(num, num * curMax, num * curMin)
            curMin = min(num, temp, num * curMin)
            res = max(res, curMax)
        return res