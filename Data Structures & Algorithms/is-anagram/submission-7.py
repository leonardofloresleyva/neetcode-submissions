class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sMap = {}
        tMap = {}
        for c in s:
            sMap[c] = 1 if c not in sMap else sMap[c] + 1
        for c in t:
            tMap[c] = 1 if c not in tMap else tMap[c] + 1
        for key in sMap:
            if key not in tMap:
                return False
            if tMap[key] != sMap[key]:
                return False
        return True