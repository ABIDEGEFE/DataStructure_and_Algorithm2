class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        triplets = []

        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = len(nums) - 1
            target = -1*nums[i]

            while l < r:
                if nums[l] + nums[r] == target:
                    triplets.append([nums[l], nums[r], nums[i]])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1

                    r -= 1
                    l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    l += 1

        return triplets


        