def NaivelongestCommonPrefix(strs):

    smallest = len(min(strs,key=len))
    lcp = ""
    character = ""
    valid = True
    
    for i in range(smallest):
        
        character = ""
        for word in strs:
            if character == "":
                character = word[i]
            else:
                if word[i] != character:
                    return lcp
                
        lcp+= character



def longestCommonPrefix(strs: list[str]):

    pre = strs[0]

    for i in strs:

        while not i.startswith(pre):
            pre = pre[:-1]

    return pre

strs = ["flower","flow","flight"]
print(longestCommonPrefix(strs))