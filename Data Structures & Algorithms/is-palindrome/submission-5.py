class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l < r:
            if (self.isAlphanum(s[l])) and (self.isAlphanum(s[r])):
                if (s[l].lower()) != (s[r].lower()):
                    return False
                l += 1
                r -= 1
            if not(self.isAlphanum(s[l])):
                l += 1
            if not(self.isAlphanum(s[r])):
                r -= 1
        return True
    def isAlphanum(self, s: str) -> bool:
            c = s.lower()
            alpha = ord(c) >= ord("a") and ord(c) <= ord("z")
            num = ord(c) >= ord("0") and ord(c) <= ord("9")
            return alpha or num