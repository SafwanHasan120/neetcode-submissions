class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False] * (len(nums))
        #[T, T, F, T, F]
        #[1, 2, 0, 1, 0]
        if len(nums) == 1:
            return True
        sinceLast = 1
        for i in range(len(nums)-2, -1, -1):
            if nums[i] >= sinceLast:
                dp[i] = True
                sinceLast = 0
            sinceLast += 1
        return dp[0]