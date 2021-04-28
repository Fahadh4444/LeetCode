class Solution:
    def uniquePathsWithObstacles(self, OG: List[List[int]]) -> int:
        if OG[0][0]:
            return 0
        m, n = len(OG), len(OG[0])
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if OG[i][j] or (i == 0 and j == 0):
                    continue
                dp[i][j] = (dp[i-1][j] if i else 0) + (dp[i][j-1] if j else 0)
        return dp[m-1][n-1]

# Code Which is excceeding Time Limit
# class Solution:
#     a = 0
#     def check(self,OG,x,y,n,m):
#         print(x,y,n,m)
#         if(y == n-1 and x == m-1):
#             self.a+=1
#             return
#         if(y > n-1 or x > m-1 or OG[y][x] == 1): return
#         return self.check(OG,x+1,y,n,m),self.check(OG,x,y+1,n,m)

#     def uniquePathsWithObstacles(self, OG: List[List[int]]) -> int:
#         n, m = len(OG), len(OG[0])
#         if(OG[n-1][m-1] == 1): return 0
#         x, y = 0, 0
#         self.check(OG,x,y,n,m)
#         return self.a
