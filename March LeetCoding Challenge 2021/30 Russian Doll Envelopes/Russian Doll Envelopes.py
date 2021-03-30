# class Solution:
#     def maxEnvelopes(self, E: List[List[int]]) -> int:
#         E.sort(key = lambda x:(x[0],-x[1]))
#         arr=[]
#         arr = [1 for i in range(len(E))]
#         for i in range(len(E)):
#             for j in range(i+1):
#                 if(E[i][0] > E[j][0] and E[i][1] > E[j][1]):
#                     arr[i] = max((arr[j]+1),arr[i])
#         return max(arr)


class Solution:
    def maxEnvelopes(self, E: List[List[int]]) -> int:
        E.sort(key=lambda x: (x[0], -x[1]))
        dp = []
        for _, height in E:
            left = bisect_left(dp, height)
            if left == len(dp):
                dp.append(height)
            else:
                dp[left] = height
        return len(dp)
