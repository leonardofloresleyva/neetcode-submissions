class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        fNums = set(nums)
        longest = 0
        for n in fNums:
            if (n - 1) not in fNums:
                length = 1
                while (n + length) in fNums:
                    length += 1
                longest = max(length, longest)
        return longest