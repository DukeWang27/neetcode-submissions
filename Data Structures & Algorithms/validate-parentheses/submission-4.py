class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')' : '(', ']' : '[', '}' : '{'}
        
        for i in s:
            if i not in pairs:
                stack.append(i)
            
            elif i in pairs:
                if not stack or stack[-1] != pairs[i]:
                    return False
                else:
                    stack.pop()
        return not stack