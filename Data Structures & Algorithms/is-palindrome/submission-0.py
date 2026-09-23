class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanum = set(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w","x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7","8", "9"])
        palindrome = []
        for c in s.lower():
            if c in alphanum:
                palindrome.append(c)
        forward = "".join(palindrome)
        palindrome.reverse()
        backwards = "".join(palindrome)
        return forward == backwards