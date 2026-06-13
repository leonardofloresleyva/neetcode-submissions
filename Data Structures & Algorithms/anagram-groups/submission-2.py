class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        anagrams = defaultdict(list)

        for i, s in enumerate(strs):
            sortString = "".join(sorted(s))
            anagrams[sortString].append(s)
        
        for val in anagrams.values():
            output.append(val)

        return output