class Solution:
    def isPalindrome(self, s: str) -> bool:
        palindrome = ""
        for c in s.lower():
            if c.isalnum():
                palindrome += c
        l = 0
        r = len(palindrome) - 1
        while l < r:
            if palindrome[l] != palindrome[r]:
                return False
            l += 1
            r -= 1
        return True