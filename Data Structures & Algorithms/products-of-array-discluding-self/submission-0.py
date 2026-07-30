class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        # Seeks out for zeros
        left = 0
        right = length - 1
        zeros = []
        while left <= right:
            if nums[left] == 0:
                zeros.append(left)
            if nums[right] == 0 and right > left:
                zeros.append(right)
            # If more than one zero is found, the result
            # is always an array of zeros
            if len(zeros) >= 2:
                return [0] * length
            left += 1
            right -= 1
        output = []
        total = nums[0]
        # If only one zero is found
        if len(zeros) == 1:
            # The position where that zero is located
            # is also the only one with a value 
            # different from zero
            output = [0] * length
            for i in range(1, length):
                if i != zeros[0]:
                    total *= nums[i]
            output[zeros[0]] = total
        # If no zero is found
        else:
            for i in range(1, length):
                total *= nums[i]
            for i in range(length):
                output.append(int(total / nums[i]))
        return output