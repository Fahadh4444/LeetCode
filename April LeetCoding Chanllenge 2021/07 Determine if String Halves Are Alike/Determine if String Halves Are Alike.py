class Solution:
    vowels = 'aeiouAEIOU'

    def halvesAreAlike(self, S: str) -> bool:
        mid, ans = len(S) // 2, 0
        for i in range(mid):
            if S[i] in self.vowels:
                ans += 1
            if S[mid+i] in self.vowels:
                ans -= 1
        return ans == 0
