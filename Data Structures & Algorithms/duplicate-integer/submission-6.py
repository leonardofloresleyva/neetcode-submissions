class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        c = None
        for n in nums:
            if n == c:
                return True
            c = n
        return False