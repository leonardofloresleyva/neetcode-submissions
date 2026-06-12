class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i, n in enumerate(nums):
            m = target - n 
            if m in map:
                j = map[m]
                return [i, j] if j > i else [j, i]
            map[n] = i
        return