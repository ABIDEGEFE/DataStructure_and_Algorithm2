class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def helper(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1

            return s[l+1:r]

        longest = ""

        for i in range(len(s)):
            oddPalindrome = helper(i, i)
            if len(oddPalindrome) > len(longest):
                longest = oddPalindrome
            evenPalindrome = helper(i, i+1)
            if len(evenPalindrome) > len(longest):
                longest = evenPalindrome

        return longest