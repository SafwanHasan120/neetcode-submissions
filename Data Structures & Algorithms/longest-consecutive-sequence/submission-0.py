class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for num in numSet:
            if(num - 1) not in numSet:
                curLength = 1
                while (num + curLength) in numSet:
                    curLength += 1
                longest = max(curLength, longest)
        return longest
