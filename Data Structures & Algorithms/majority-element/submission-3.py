class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        for i, n in enumerate(nums):
            j = i - 1
            count = count + 1 if j >= 0 and nums[j] == n else 1
            if count > len(nums) / 2:
                return n