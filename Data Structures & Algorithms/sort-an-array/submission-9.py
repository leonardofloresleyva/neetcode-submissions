# Math library to obtain absolute values from negative numbers
import math

class Solution:
    # RadixSort implementation (v3)
    def sortArray(self, nums: List[int]) -> List[int]:

        # Radix buckets array
        rdxArr = [[], [], [], [], [], [], [], [], [], []]
        
        # Number with the highest value
        k = max(nums)

        # Exponent
        exp = 1

        # If the highest value is negative
        if k < 0:
            k = math.fabs(min(nums))
            while k // exp > 0:
                # Places the values in their buckets
                while len(nums) > 0:
                    val = nums.pop()
                    # The value is placed in reverse order
                    rdxArr[9 - (int(math.fabs(val)) // exp) % 10].append(val)

                # Puts back the sorted values in the original array
                for bucket in rdxArr:
                    while len(bucket) > 0:
                        val = bucket.pop()
                        nums.append(val)
                        
                # Increases the exponent by 10 times
                exp *= 10
        else:
            # Number with the lowest value
            minValue = min(nums)

            # If the lowest value is negative
            if minValue < 0:

                rdxArrNegatives = [[], [], [], [], [], [], [], [], [], []]

                if len(str(minValue)[1:]) > len(str(k)):
                    k = math.fabs(minValue)

                while k // exp > 0:

                    # Places the values in their buckets
                    while len(nums) > 0:
                        val = nums.pop()
                        if val < 0:
                            # If negative, the value is placed in reverse order
                            rdxArrNegatives[9 - (int(math.fabs(val)) // exp) % 10].append(val)
                        else:
                            rdxArr[(val // exp) % 10].append(val)

                    # Puts back the sorted negative values in the original array first
                    for bucket in rdxArrNegatives:
                        while len(bucket) > 0:
                            val = bucket.pop()
                            nums.append(val)

                    # Puts back the sorted positive values in the original array
                    for bucket in rdxArr:
                        while len(bucket) > 0:
                            val = bucket.pop()
                            nums.append(val)
                            
                    # Increases the exponent by 10 times
                    exp *= 10
            # All numbers are higher than zero
            else:
                while k // exp > 0:
                    # Places the values in their buckets
                    while len(nums) > 0:
                        val = nums.pop()
                        rdxArr[(val // exp) % 10].append(val)

                    # Puts back the sorted values in the original array
                    for bucket in rdxArr:
                        while len(bucket) > 0:
                            val = bucket.pop()
                            nums.append(val)
                            
                    # Increases the exponent by 10 times
                    exp *= 10
                
        # Returns the sorted array
        return nums