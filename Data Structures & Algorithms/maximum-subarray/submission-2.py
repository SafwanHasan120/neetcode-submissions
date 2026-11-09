class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        memo = {}
        def bt(i, check):
            if i >= len(nums)-1:
                if check:
                    return max(0, nums[i])
                else:
                    return nums[i]
            if (i, check) in memo:
                return memo[(i, check)]
            if check:
                res = max(0, nums[i] + bt(i+1, True))
                memo[(i, check)] = res
                return res
            res = max(bt(i+1, False), nums[i] + bt(i+1, True))
            memo[(i, check)] = res
            return res
            
        return bt(0, False)