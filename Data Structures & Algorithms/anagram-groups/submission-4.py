class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            sortString = "".join(sorted(s))
            anagrams[sortString].append(s)
        return list(anagrams.values())