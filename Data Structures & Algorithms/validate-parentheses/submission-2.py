class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        bracket_matches = {
            "(": ")",
            "{": "}",
            "[": "]"
        }

        for character in s:
            if character in bracket_matches:
                stack.append(character)
            else:
                if not stack: # if the stack is empty
                    return False
                if bracket_matches[stack[-1]] != character:
                    return False
                stack.pop()
                

        return not stack