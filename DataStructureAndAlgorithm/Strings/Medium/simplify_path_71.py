class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        for part in path.split('/'):
            if part == "" or part == ".":
                continue
            if part == ".." and stack:
               stack.pop()
            if not part == "..":
                stack.append(part) 
               

        return "/" + "/".join(stack)
        