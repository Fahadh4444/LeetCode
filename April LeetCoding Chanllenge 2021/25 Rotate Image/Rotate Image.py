class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l = len(matrix)
        for i in range(l):
            for j in range(i, l):
                a = matrix[j][i]
                matrix[j][i] = matrix[i][j]
                matrix[i][j] = a
        for i in range(l):
            for j in range(l//2):
                a = matrix[i][l-j-1]
                matrix[i][l-j-1] = matrix[i][j]
                matrix[i][j] = a
