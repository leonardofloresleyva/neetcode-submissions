class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        curr = - 1
        count = 0
        for i, n in enumerate(nums):
            curr = n
            j = i - 1
            if j >= 0 and nums[j] == curr:
                count += 1
                if count > len(nums) / 2:
                    return curr
            else:
                count = 1
        return curr