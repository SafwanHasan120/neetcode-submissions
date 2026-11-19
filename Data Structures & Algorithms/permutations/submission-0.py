class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def bt(numsLeft, out):
            if not numsLeft:
                res.append(out)
                return
            for i in range(len(numsLeft)):
                temp = numsLeft.pop(i)
                bt(numsLeft, out = out + [temp])
                numsLeft.insert(i, temp)
        bt(nums, [])
        return res