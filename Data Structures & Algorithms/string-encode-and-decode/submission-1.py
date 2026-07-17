class Solution:
    # Hint 3 solution
    def encode(self, strs: List[str]) -> str:
        solution = ''
        for s in strs:
            l = len(s)
            solution += f"{l}#{s}"
        return solution

    def decode(self, s: str) -> List[str]:
        strList = []
        # Two pointers
        i = 0
        j = 0
        ending = len(s)
        while i < ending:
            if s[j] == "#":
                left = j + 1
                end = left + int(s[i:j])
                strList.append(s[left:end])
                i = j = end
            else:
                j += 1
        return strList