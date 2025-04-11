def isPalindrome(x):
    num = str(x)

    l = 0
    r = len(num) - 1
    while l < r:
        if num[l] != num[r]:
            return False
        else:
            l+=1
            r-=1

    return True

x = 101
print(isPalindrome(x))
