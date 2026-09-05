class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxHeight = 0
        left = 0
        right = len(heights) - 1
        while left < right:
            area = min(heights[left], heights[right]) * (right - left)
            maxHeight = max(maxHeight, area)
            if(heights[left] > heights[right]):
                right -= 1
            else:
                left += 1
        return maxHeight