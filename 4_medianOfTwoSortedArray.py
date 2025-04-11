def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    merged = []
    indexNums1 = 0
    indexNums2 = 0

    for i in range(len(nums1) + len(nums2)):

        if indexNums1 < len(nums1) and indexNums2 < len(nums2):
            if nums1[indexNums1] < nums2[indexNums2]:
                merged.append(nums1[indexNums1])
                indexNums1+=1
            else:
                merged.append(nums2[indexNums2])
                indexNums2+=1
            
        elif indexNums1 < len(nums1):
            merged.append(nums1[indexNums1])
            indexNums1+=1
        elif indexNums2 < len(nums2):
            merged.append(nums2[indexNums2])
            indexNums2+=1


    if len(merged) % 2 == 0:
        num1 = merged[(len(merged)//2)-1]
        num2 = merged[(len(merged)//2)]

        print(num1)
        print(num2)

        return (num1+num2)/2
    else:
        return float(merged[len(merged)//2])

        
    


nums1 = [1,2]
nums2 = [3,4]

print(findMedianSortedArrays(nums1,nums2))