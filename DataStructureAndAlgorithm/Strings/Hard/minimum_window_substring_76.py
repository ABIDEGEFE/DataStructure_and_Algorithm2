class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: st
        :type t: str
        :rtype: str
        """
        Ofreq = {}
        for i in t:
            Ofreq[i] = Ofreq.get(i, 0) + 1

        window = {}
        l = r = formed = 0
        target = len(Ofreq)
        min_len = float("inf")
        result = ""
                
        while r < len(s):
            window[s[r]] = window.get(s[r], 0) + 1
            if s[r] in Ofreq and window[s[r]] == Ofreq[s[r]]:
                formed += 1

            while formed == target and l <= r:
                curLength = r-l+1
                if curLength < min_len:
                    min_len = curLength
                    result = s[l:r+1]

                window[s[l]] -= 1
                if s[l] in Ofreq and window[s[l]] < Ofreq[s[l]]:
                    formed -= 1
                l += 1
            
            r += 1

        return result
 
        