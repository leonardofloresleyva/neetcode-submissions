class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        anagrams = {}

        for i, s in enumerate(strs):
            sortString = "".join(sorted(s))
            if sortString in anagrams:
                anagrams[sortString].append(s)
            else:
                anagrams[sortString] = [s]
        
        for val in anagrams.values():
            output.append(val)

        return output