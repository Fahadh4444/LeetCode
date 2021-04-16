class Solution:
    def removeDuplicates(self, S: str, K: int) -> str:
        count, i = 1, 1
        while i < len(S):
            if S[i] == S[i-1]:
                count += 1
            else:
                count = 1
            if count == K:
                S = self.removeDuplicates(S[:i-K+1] + S[i+1:], K)
            i += 1
        return S
