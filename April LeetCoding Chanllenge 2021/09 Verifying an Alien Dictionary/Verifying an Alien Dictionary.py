class Solution:
    def isAlienSorted(self, W: List[str], O: str) -> bool:
        alpha = {O[i]: i for i in range(len(O))}
        for i in range(1, len(W)):
            a, b = W[i-1], W[i]
            for j in range(len(a)):
                if j == len(b):
                    return False
                achar, bchar = a[j], b[j]
                aix, bix = alpha[achar], alpha[bchar]
                if aix < bix:
                    break
                if aix > bix:
                    return False
        return True


# ///////////////////////////////JavaSScript Code/////////////////////////////////////
# var isAlienSorted = function(W, O) {
#     let alpha = new Map([["",-1]])
#     for (let i = 0; i < O.length; i++)
#         alpha.set(O.charAt(i), i)
#     for (let i = 1; i < W.length; i++) {
#         let a = W[i-1], b = W[i]
#         for (let j = 0; j < a.length; j++) {
#             let achar = a.charAt(j), bchar = b.charAt(j),
#                 aix = alpha.get(achar), bix = alpha.get(bchar)
#             if (aix < bix) break
#             if (aix > bix) return false
#         }
#     }
#     return true
# };
