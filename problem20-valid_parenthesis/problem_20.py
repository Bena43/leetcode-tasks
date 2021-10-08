class Solution:
    def isValid(self, s: str) -> bool:
        expected = []
        for c in s:
            if c in ['(', '[', '{']:
                # if parenthesis opener, add it's closer in the first item of the "Expected" list
                if c == '(':
                    expected.insert(0, ')')
                elif c == "[":
                    expected.insert(0, ']')
                elif c == "{":
                    expected.insert(0, '}')
            else:
                # if parenthesis closer, check if it is the expected closer (the matching closer of the previous opener)
                if not expected:
                    # If not expecting a closer, string is wrong, return false
                    return False
                if expected[0] != c:
                    # Not the expected closer, string is wrong, return false
                    return False
                else:
                    # Correct closer, remove it from list and continue checking the list
                    expected = expected[1:]
            
        if expected:
            return False
        else:
            return True