class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output = set()
        topK = {}

        # Substracting nums items
        while len(nums) > 0: 
            n = nums.pop()
            topK[n] = topK[n] + 1 if n in topK else 1
        
        while len(output) < k:
            top = 0
            chosen = None
            for n in topK:
                if topK[n] >= top and n not in output:
                    top = topK[n]
                    chosen = n
            output.add(chosen)
        
        return list(output)