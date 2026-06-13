class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Two pointers
        i = 0
        j = len(nums) - 1
        # In-place removal
        while i <= j:
            if nums[i] == val:
                nums.pop(i)
                if i == j:
                    break
                else:
                    j -= 1
            else:
                i += 1
            if nums[j] == val:
                nums.pop(j)
            j -= 1
        # Only k-values left
        return len(nums)