class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        # Inner function that searches for zeros
        def findZeros(nums: List[int]) -> List[int]:
            zeros = []
            left = 0
            right = length - 1
            while left <= right:
                if nums[left] == 0:
                    zeros.append(left)
                if nums[right] == 0 and right > left:
                    zeros.append(right)
                # If more than one zero is found, the loop is ended
                if len(zeros) >= 2:
                    break
                left += 1
                right -= 1
            return zeros
        # Array of zeros
        zeros = findZeros(nums)
        # If more than one zero is found, the result is always an
        # array of zeros of size n
        if len(zeros) >= 2:
            return [0] * length
        else:
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