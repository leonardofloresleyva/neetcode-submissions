class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        l, r = 0, len(numbers) - 1
        twoSum = numbers[l] + numbers[r]
        while twoSum != target:
            while twoSum > target:
                r -= 1
                twoSum = numbers[l] + numbers[r]
            while twoSum < target:
                l += 1
                twoSum = numbers[l] + numbers[r]
        return [l + 1, r + 1]