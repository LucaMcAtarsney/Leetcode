def lengthOfLongestSubstring(s):
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


s = "abcabcbb"
print(lengthOfLongestSubstring(s))