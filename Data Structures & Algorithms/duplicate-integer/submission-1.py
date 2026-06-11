class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        n = None
        for i in range(len(nums)):
            if nums[i] == n:
                return True
            n = nums[i]
        return False