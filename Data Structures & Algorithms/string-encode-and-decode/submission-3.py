class Solution:
    # Less readable solution, but less code
    def encode(self, strs: List[str]) -> str:
        solution = ""
        for s in strs:
            solution += str(len(s)) + "%" + s
        return solution

    def decode(self, s: str) -> List[str]:
        strList, i, j, end = [], 0, 0, len(s)
        while i < end:
            if s[j] == "%":
                length = int(s[i:j])
                strList.append(s[j + 1 : j + 1 + length])
                i = j = j + 1 + length
                continue
            j += 1
        return strList