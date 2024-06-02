class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]
        lastRow = result[0]
        for row in range(1, numRows):
            lastRow = [sum(v) for v in zip([0] + lastRow, lastRow + [0])]
            result.append(lastRow)
        return result
