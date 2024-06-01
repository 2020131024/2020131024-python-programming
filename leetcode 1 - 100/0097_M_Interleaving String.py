class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        len1, len2, len3 = len(s1), len(s2), len(s3)

        if len1 + len2 != len3:
            return False

        stack = [(0, 0)]
        visit = set()

        while stack:
            i, j = stack.pop(-1)

            if i+j == len3:
                return True

            if i < len1 and s1[i] == s3[i+j] and (i+1, j) not in visit:
                stack.append((i+1, j))
                visit.add((i+1, j))

            if j < len2 and s2[j] == s3[i+j] and (i, j+1) not in visit:
                stack.append((i, j+1))
                visit.add((i, j+1))

        return False
