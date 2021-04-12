import math


class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        arr = []
        if(k % 2 == 1):
            m = math.ceil(k/2)+1
        if(k % 2 == 0):
            m = math.ceil(k/2)+2
        for i in range(1, m):
            arr.append(i)
            if(i != (k+2)-i):
                arr.append(k+2-i)
        if(k+1 < n):
            for j in range(k+2, n+1):
                arr.append(j)
        return arr
