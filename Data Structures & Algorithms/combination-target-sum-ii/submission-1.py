class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def bt(i, curSum, soFar):
            if curSum == target:
                res.append(soFar)
                return
            if curSum > target or i >= len(candidates):
                return
            bt(i+1, curSum + candidates[i], soFar + [candidates[i]])
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            bt(i+1, curSum, soFar)
        bt(0, 0, [])
        return res
            