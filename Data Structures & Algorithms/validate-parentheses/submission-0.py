class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pMap = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }

        # loop through array of parentheses
        for char in s:
            # if parentheses is one of the pMap keys
            if char in pMap:
                # if the stack has something in it, and the top of it is the opposite to the array parentheses
                if stack and stack[-1] == pMap[char]:
                    # pop the bracket in the stack
                    stack.pop()
                else:
                    # or, return false as it isnt matching
                    return False
            else:
                # add the opening bracket to the stack
                stack.append(char)

        return not stack