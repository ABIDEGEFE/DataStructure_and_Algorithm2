class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        result = 10**5
        gap = 10**5
        nums = sorted(nums)
        for i in range(len(nums)-2):
            # print(i, nums[i])
            l = i + 1
            r = len(nums)-1

            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total == target:
                    return total

                diff = total - target
                if diff < 0:
                    diff = -1 * diff
                if diff < gap:
                    result = total
                    gap = diff

                if total > target:
                    r -= 1
                else:
                    l += 1

        return result
        