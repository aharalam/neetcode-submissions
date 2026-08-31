class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        brackets = {
            "(": ")",
            "{": "}",
            "[": "]"
        }

        for character in s:
            if character in brackets:
                stack.append(character)
            else:
                if not stack:
                    return False
                if brackets[stack[-1]] != character:
                    return False
                stack.pop()

        return not stack
