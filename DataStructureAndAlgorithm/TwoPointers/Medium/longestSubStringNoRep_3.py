class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0

        freq = {}
        p = leng = 0
        # width = (0, 1)
        x = 0
        
        for i in range(len(s)):
            freq[s[i]] = freq.get(s[i], 0) + 1
            if freq[s[i]] > 1:
                if (i-p) > leng:
                    # width = (p, i)
                    leng = i-p
                
                while s[p] != s[i]:
                    del freq[s[p]]
                    p += 1
                p += 1
                freq[s[i]] -= 1
            x = i
        # print(width[0], width[1])
        return max(leng, x-p+1)

               

