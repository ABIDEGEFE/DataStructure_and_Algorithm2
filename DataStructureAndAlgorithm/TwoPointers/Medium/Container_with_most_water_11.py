class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        area = 0

        while left < right:
            y = min(height[left], height[right])
            if y * (right-left) > area:
                area = y * (right - left)

            if y == height[left]:
                left += 1
            else:
                right -= 1

        return area
        