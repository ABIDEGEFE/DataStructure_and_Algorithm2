class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hash_count = {}

        for i in s:
            hash_count[i] = hash_count.get(i, 0) + 1

        for i in t:
            hash_count[i] = hash_count.get(i, 0) - 1
            if hash_count[i] == 0:
                del hash_count[i]

        return len(hash_count) == 0
    

# time complexity: O(n)
# space complexity: O(n)
             
        