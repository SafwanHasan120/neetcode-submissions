class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement = {}
        for i in range(len(nums)):
            if((target - nums[i]) in complement):
                return [complement.get(target - nums[i]), i]
            else:
                complement[nums[i]] = i
        return [0, 0]