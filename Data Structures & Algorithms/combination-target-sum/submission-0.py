class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        soFar = []
        memo = {}

        def bt(i, curSum, soFar):
            if curSum > target or i >= len(nums):
                return
            if curSum == target:
                res.append(soFar)
            else:
                

                bt(i+1, curSum, soFar)
                bt(i, curSum + nums[i], soFar + [nums[i]])
        bt(0, 0, [])
        return res
