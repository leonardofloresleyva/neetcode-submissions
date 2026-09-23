class Solution:
    def isPalindrome(self, s: str) -> bool:
        palindrome = []
        for c in s.lower():
            if c.isalnum():
                palindrome.append(c)
        forward = "".join(palindrome)
        palindrome.reverse()
        backwards = "".join(palindrome)
        return forward == backwards