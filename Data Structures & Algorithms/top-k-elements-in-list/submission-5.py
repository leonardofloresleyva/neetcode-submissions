class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Sorting solution
        if len(nums) == 1:
            return [nums[0]]
        
        nums.sort()
        topK = [[1, nums[0]]]
        
        for i in range(1, len(nums)):
            if nums[i] == topK[-1][1]:
                topK[-1][0] += 1
            else:
                topK.append([1, nums[i]])
        
        topK.sort()
        
        res = []
        while len(res) < k:
            res.append(topK.pop()[1])

        return res