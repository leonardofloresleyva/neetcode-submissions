class Solution:
    def isPalindrome(self, s: str) -> bool:
        l , r = 0, len(s) - 1
        while l < r:
            while l < r and not self.isAlphanum(s[l]):
                l += 1
            while l < r and not self.isAlphanum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
    
    def isAlphanum(self, c: str) -> bool:
            return (ord(c) >= ord("a") and ord(c) <= ord("z")) or (ord(c) >= ord("A") and ord(c) <= ord("Z")) or (ord(c) >= ord("0") and ord(c) <= ord("9"))