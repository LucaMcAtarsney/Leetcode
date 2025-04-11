def NaiveLengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    maxLength = 0
    buffer = ""
    offset = 0

    for i in range(len(s)):

        if s[i] not in buffer:
            buffer+= s[i]
        else:
            offset = 0

            while s[i] in buffer:
                buffer = buffer[1:]
                offset += 1

            buffer = buffer + s[i]
            i+=offset

        if len(buffer) > maxLength:
            maxLength = len(buffer)

    return maxLength

def LengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
   
    seen = {}
    l = 0
    output = 0

    for r in range(len(s)):

        if s[r] not in seen:
            output = max(output,r-l+1)
        else:
            if seen[s[r]] < l:
                output = max(output,r-l+1)
            else:
                l = seen[s[r]] + 1

        seen[s[r]] = r

    return output



s = "abcabcbb"
print(NaiveLengthOfLongestSubstring(s))
print(LengthOfLongestSubstring(s))