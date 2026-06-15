class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # This is copy-pasted from other user's solution, but without
        # some unnecesary variables. Credits to its original author
        # (I'd never pull this solution out on my first day haha)
        set_nums = set(nums)
        dict_nums = {num: nums.count(num) for num in set_nums}
        return sorted(dict_nums.items(), key = lambda item: item[1], reverse=True)[0][0]