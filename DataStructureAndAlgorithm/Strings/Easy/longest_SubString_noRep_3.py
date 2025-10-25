class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0 or len(s) == 1:
            return len(s) 

        freq = {}
        leng = 0
        count = 0
        result = 0
        start = 0

        while count < len(s):
            freq[s[count]] = freq.get(s[count], 0) + 1
            if freq[s[count]] > 1:
                
                while s[count] != s[start]:
                    del freq[s[start]]
                    start += 1

                start += 1
                freq[s[count]] -= 1
                result = max(leng, result)
                leng = count - start

            count += 1
            leng += 1

        return max(leng, result)