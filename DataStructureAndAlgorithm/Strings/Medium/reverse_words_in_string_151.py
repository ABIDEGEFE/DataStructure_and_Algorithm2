class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        words = s.split()
        l, r = 0, len(words)-1

        while l < r:
            words[l], words[r] = words[r], words[l]
            l += 1
            r -= 1

        return " ".join(words)
        