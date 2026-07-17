class Solution:
    # Hint 3 solution
    def encode(self, strs: List[str]) -> str:
        solution = ""
        for s in strs:
            l = len(s)
            solution += f"{l}%{s}"
        return solution

    def decode(self, s: str) -> List[str]:
        strList = []
        # Two pointers
        i = 0
        j = 0
        end = len(s)
        # Looping through the full string
        while i < end:
            if s[j] == "%":
                left = j + 1
                right = left + int(s[i:j])
                strList.append(s[left:right])
                i = j = right
                continue
            j += 1
        return strList