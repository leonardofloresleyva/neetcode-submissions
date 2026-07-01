# Math library to obtain absolute values from negative numbers
import math

class Solution:
    # MergeSort implementation (v2)
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]

        sortedLeft = self.sortArray(left)
        sortedRight = self.sortArray(right)
        return self.merge(sortedLeft, sortedRight)
    
    def merge(self, left: List[int], right: List[int]) -> List[int]:
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])

        return result