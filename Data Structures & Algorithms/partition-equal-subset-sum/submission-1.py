class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        #1, 2, 3, 4, 1, 1
        #Look at current comparison, if its bigger, add cur pointer to original and keep moving
        #DP array with true/false values, and for each iteration you would look at sums. 
        total = sum(nums)
        if total % 2:
            return False
        target = total // 2

        memo = {}

        def bt(i, need):
            if need == 0:
                return True
            if need < 0 or i == len(nums):
                return False
            if (i, need) in memo:
                return memo[(i, need)]
            
            res = bt(i + 1, need - nums[i]) or bt(i + 1, need)
            memo[(i, need)] = res
            return res

        return bt(0, target)
        