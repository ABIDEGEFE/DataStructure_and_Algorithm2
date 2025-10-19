class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        original = x
        reversed_sum = 0

        while x > 0:
            modulo = x % 10
            reversed_sum = reversed_sum * 10 + modulo

            x = x//10
        
        return original == reversed_sum