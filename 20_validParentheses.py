class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        parentheses = {')':'(','}':'{',']':'['}

        stack = []

        for i in range(len(s)):

            if s[i] not in parentheses:
                stack.append(s[i])
            else:
                if stack != []:
                    if parentheses[s[i]] != stack.pop():
                        return False
                else:
                    return False

        if stack == []:
            return True
        else:
            return False
    