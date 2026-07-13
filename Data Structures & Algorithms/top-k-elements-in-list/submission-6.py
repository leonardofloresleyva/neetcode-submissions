class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Sorting solution (removes elements from nums while iterating)
        if len(nums) == 1:
            return [nums[0]]
        
        nums.sort()
        topK = [[1, nums.pop(0)]]

        while len(nums) > 0:
            n = nums.pop(0)
            if n == topK[-1][1]:
                topK[-1][0] += 1
            else:
                topK.append([1, n])
        
        topK.sort()
        
        res = []
        while len(res) < k:
            res.append(topK.pop()[1])

        return res