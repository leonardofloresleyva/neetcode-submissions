class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxWater = -1
        left = 0
        right = len(heights) - 1
        while left < right:
            width = right - left
            height = min(heights[left], heights[right])
            water = width * height
            maxWater = water if water > maxWater else maxWater

            right -= 1 if heights[right] == height else 0
            left += 1 if heights[left] == height else 0
        return maxWater