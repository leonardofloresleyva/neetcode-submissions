class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if(len(nums) > 0):
            nums.sort()
            n = nums[0]
            for i in range(1, len(nums)):
                if(nums[i] == n):
                    return True
                n = nums[i]
        return False