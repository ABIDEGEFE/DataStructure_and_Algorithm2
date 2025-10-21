class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        result = 0
        sign = 1
        if not s:
            return 0

        i = 0
        if s[i] == "-":
            sign = -1
            i += 1
        elif s[i] == "+":
            sign = 1
            i += 1
        
        while i < len(s) and s[i].isdigit():
            digit = int(s[i])
            result = result * 10 + digit

            if result * sign > 2**31 - 1:
                return 2**31 - 1
            if result * sign < -2**31:
                return -2**31

            i += 1

        return sign * result
        
            


        