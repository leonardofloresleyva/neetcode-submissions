class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        for n in range(2):
            j = len(nums) - 1
            while i < j:
                if nums[i] == n:
                    i += 1
                else:
                    if nums[j] == n:
                        nums[i], nums[j] = nums[j], nums[i]
                        i += 1
                    j -= 1