class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        final_list = set(candyType)
        return min(len(final_list), ((len(candyType))//2))
