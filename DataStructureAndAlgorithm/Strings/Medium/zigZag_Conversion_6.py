class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        result = [[] for _ in range(numRows)]
        count = 0
        forward = True
        for cr in s:
            # print(cr)
            if forward:
                result[count].append(cr)
                count += 1
            else:
                count -= 1
                result[count].append(cr)

            if count >= numRows:
                forward = False
                count = numRows - 1

            if count <= 0:
                forward = True
                count += 1
            
        print(result)
        zigzag = []
        for i in result:
            zigzag += i

        return "".join(zigzag)