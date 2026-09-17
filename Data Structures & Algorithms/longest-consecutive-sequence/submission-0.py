class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums.sort()
        longestSequence = 0
        currentSequence = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                continue
            diff = nums[i] - nums[i - 1]
            if diff == 1:
                currentSequence += 1
            else:
                if currentSequence > longestSequence:
                    longestSequence = currentSequence
                currentSequence = 1
        return longestSequence if longestSequence > currentSequence else currentSequence