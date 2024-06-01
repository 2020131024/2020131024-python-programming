class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if matrix == []: return 0
        else:
            mat = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
            for i in range(len(matrix)):
                for j in range(len(matrix[i])):
                    if matrix[i][j] == "1":
                        hei = 0
                        idx = i
                        while idx < len(matrix):
                            if matrix[idx][j] == "1":
                                hei += 1
                            else: break
                            idx += 1
                        mat[i][j] = hei
            result = 0
            for i in range(len(mat)):
                stack = [[0, mat[i][0]]]
                for j in range(1, len(mat[i])):
                    idx = j
                    while stack != [] and stack[-1][1] > mat[i][j]:
                        val = stack[-1][1] * (j - stack[-1][0])
                        if result < val: result = val
                        idx = stack.pop()[0]
                    stack.append([idx, mat[i][j]])
                while stack != []:
                    val = stack[-1][1] * (len(mat[i]) - stack[-1][0])
                    if result < val: result = val
                    stack.pop()
            return result
