class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        s = s.strip()
        words = s.split()
        space = 0
        result = []
        for i in range(len(words)-1, -1, -1):
            if words[i]:
                space = 0

            if not words[i] and space == 1:
                continue
            if not words[i]:
                space = 1

            result.append(words[i])

        return " ".join(result)
        