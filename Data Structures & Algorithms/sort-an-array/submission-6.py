# Math library to obtain absolute values from negative numbers
import math

class Solution:
    # RadixSort implementation
    def sortArray(self, nums: List[int]) -> List[int]:
        
        # Radix buckets array
        rdxArrPositives = [[], [], [], [], [], [], [], [], [], []]
        rdxArrNegatives = [[], [], [], [], [], [], [], [], [], []]
        
        # Number with the highest value
        k = max(nums)

        # Checks the number with most digits (including negatives)
        if k < 0:
            k = min(nums)
        else:
            minValue = min(nums)
            if minValue < 0 and len(str(minValue)[1:]) > len(str(k)):
                k = minValue

        # Exponent
        exp = 1

        # Moves among digits from the least significant to the most
        # (The higher the exponent, the most significant the digit is)
        while math.fabs(k) // exp > 0:

            # Places the values in their buckets
            while len(nums) > 0:
                val = nums.pop()
                if val < 0:
                    # If negative, the value is placed in reverse order
                    rdxArrNegatives[9 - (int(math.fabs(val)) // exp) % 10].append(val)
                else:
                    rdxArrPositives[(val // exp) % 10].append(val)

            # Puts back the sorted negative values in the original array first
            for bucket in rdxArrNegatives:
                while len(bucket) > 0:
                    val = bucket.pop()
                    nums.append(val)

            # Puts back the sorted positive values in the original array
            for bucket in rdxArrPositives:
                while len(bucket) > 0:
                    val = bucket.pop()
                    nums.append(val)
                    
            # Increases the exponent by 10 times
            exp *= 10
            
        # Returns the sorted array
        return nums