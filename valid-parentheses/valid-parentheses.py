class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', ']':'[', '}':'{'}
        for char in s:
            if char in pairs and len(stack)>0:
                top = stack[0]
                if pairs[char] != top:
                    return False
                # otherwise take it off the stack
                else:
                    stack.pop(0)
            else:
                stack.insert(0, char)
        if len(stack) > 0:
            return False
        return True
            
                