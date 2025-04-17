class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        lp = 0
        rp = len(height)-1
        maxCap = 0
        cap = 0

        while lp < rp:

            width = rp - lp
            cap = min(height[lp],height[rp]) * width
            maxCap = max(cap,maxCap)

            if height[lp] > height[rp]:
                rp-=1
            else:
                lp+=1

        return maxCap

            