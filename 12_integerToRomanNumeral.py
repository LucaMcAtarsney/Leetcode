def intToRoman(num):
    """
    :type num: int
    :rtype: str
    """

    romanNumerals = {1:"I",5:"V",10:"X",50:"L",100:"C",500:"D",1000:"M"}

    if num in romanNumerals:
        return romanNumerals[num]
    
    
    l = {}
    if num >= 1000:
        d, r = divmod(num,1000)
        l[1000] = d
        num = r
    else:
        l[1000] = 0

    if num >= 500:
        d, r = divmod(num,500)
        l[500] = d
        num = r
    else:
        l[500] = 0

    if num >= 100:
        d, r = divmod(num,100)
        l[100] = d
        num = r
    else:
        l[100] = 0

    if num >= 50:
        d, r = divmod(num,50)
        l[50] = d
        num = r
    else:
        l[50] = 0

    if num >=10:
        d, r = divmod(num,10)
        l[10] = d
        num = r
    else:
        l[10] = 0

    if num >=5:
        d, r = divmod(num,5)
        l[5] = d
        num = r
    else:
        l[5] = 0

    if num >=1:
        d, r = divmod(num,1)
        l[1] = d
        num = r
    else:
        l[1] = 0

    numbers = [1000,500,100,50,10,5,1]
    roman = ""

    print(l)

    for x in numbers:
        instances = l[x]
        index = numbers.index(x)
        print(index)

        if x in [1,10,100,1000]:
            if instances > 3:
                #change instances to 1
                l[x] = 1

                #add instance of previous to plus 1
                l[numbers[index-1]] += l[numbers[index-1]] + 1



    print(l)

print(intToRoman(3749))