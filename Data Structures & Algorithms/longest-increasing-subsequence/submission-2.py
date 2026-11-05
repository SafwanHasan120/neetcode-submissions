class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        memo = {}
        
        def bt(i, prev):
            if (i == (len(nums))):
                return 0

            if((i, prev) in memo):
                return memo[(i, prev)]
            res = 0
            if(nums[i] <= prev):
                res = bt(i+1, prev)
            else:
                res = max(1 + bt(i+1, nums[i]), bt(i+1, prev))
            memo[(i, prev)] = res
            return res
        
        return bt(0, -1001)