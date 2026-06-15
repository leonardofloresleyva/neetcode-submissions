class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # I can't believe I didn't come up with this one :'v
        nums.sort()
        return nums[len(nums) // 2]