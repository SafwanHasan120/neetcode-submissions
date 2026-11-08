class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] <= nums[hi]:
                hi = mid
            else:
                lo = mid + 1
        pivot = hi
        if target <= nums[len(nums) - 1] and target >= nums[pivot]:
            lo, hi = pivot, len(nums)-1
        else:
            lo, hi = 0, pivot-1
        
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return -1

        