class Solution:
    # Hint 3 solution
    def encode(self, strs: List[str]) -> str:
        solution = ""
        for s in strs:
            l = len(s)
            solution += f"{l}%{s}"
        return solution

    def decode(self, s: str) -> List[str]:
        # Array solution, two pointers, and input string delimiter
        strList, i, j, end = [], 0, 0, len(s)
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