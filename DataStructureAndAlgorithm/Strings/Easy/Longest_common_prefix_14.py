class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 1:
            return strs[0]
        
        result = ""
        min_leng = min(len(s) for s in strs)

        for i in range(min_leng):
            prefix = strs[0][i]
            for j in range(1, len(strs)):
                if prefix != strs[j][i]:
                    return result
                # if prefix != strs[j][i] and result:
                #     return result
            
            result += prefix

        return result