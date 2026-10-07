class Solution:
    def rob(self, nums: List[int]) -> int:
        if(not nums):
            return 0
        if(len(nums) == 1):
            return nums[-1]
        if(len(nums) == 2):
            return max(nums[0], nums[1])

        dp = [0] * (len(nums)-1)
        dp[0] = nums[0]
        dp[1] = max(dp[0], nums[1])
        for i in range(2, len(nums)-1):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        
        dp2 = [0]
        dp2 = [0] * (len(nums)-1)
        dp2[0] = nums[1]
        dp2[1] = max(dp2[0], nums[2])
        for i in range(3, len(nums)):
            dp2[i-1] = max(dp2[i-2], dp2[i-3] + nums[i])
        return max(dp[-1], dp2[-1])