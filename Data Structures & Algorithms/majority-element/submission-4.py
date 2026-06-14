class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        res = nums[0]
        count = 1
        for i in range(1, len(nums)):
            if nums[i - 1] == nums[i]:
                count += 1
                if count > len(nums) / 2:
                    res = nums[i]
                    break
            else:
                count = 1
        return res