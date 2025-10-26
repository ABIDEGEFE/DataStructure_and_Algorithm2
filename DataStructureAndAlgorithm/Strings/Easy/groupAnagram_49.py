class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        freq = {}
        
        for i in strs:
            count = [0] * 26
            for j in i:
                count[ord(j) - ord('a')] += 1

            key = tuple(count)
            if key in freq:
                freq[key].append(i)
            else:
                freq[key] = [i]

        return list(freq.values())

                