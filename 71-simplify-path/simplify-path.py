class Solution(object):
    def simplifyPath(self, path):
        stack = []

        parts = path.split("/")

        for folder in parts:
            if folder == "" or folder == ".":
                continue

            elif folder == "..":
                if stack:
                    stack.pop()

            else:
                stack.append(folder)

        return "/" + "/".join(stack)