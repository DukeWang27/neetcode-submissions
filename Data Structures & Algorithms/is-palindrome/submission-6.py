class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanedStr = ""
        for i in range(len(s)):
            if s[i].isalnum():
                cleanedStr += s[i].lower()
        
        if cleanedStr[::-1] == cleanedStr:
            return True
        else:
            return False