class Solution:
    def isPalindrome(self, s: str) -> bool:
        #sol 1
        '''cleanedStr = ""
        for i in range(len(s)):
            if s[i].isalnum():
                cleanedStr += s[i].lower()
        
        if cleanedStr[::-1] == cleanedStr:
            return True
        else:
            return False'''

        #sol 2
        start = 0
        end = len(s) - 1

        while start < end:
            if not s[start].isalnum():
                start += 1
                continue

            if not s[end].isalnum():
                end -= 1
                continue

            if s[start].lower() != s[end].lower():
                return False
            
            start += 1
            end -= 1
        
        return True

        


