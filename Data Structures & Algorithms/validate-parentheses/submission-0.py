class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict_close = {")":"(", "]":"[", "}":"{"}

        for i in s:
            if i in dict_close:
                if stack and stack[-1] == dict_close[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False