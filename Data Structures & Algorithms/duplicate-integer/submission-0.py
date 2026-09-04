class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        cur = set()
        for num in nums:
            if num in cur:
                return True
            else:
                cur.add(num)
        return False