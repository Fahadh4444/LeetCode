class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        ans, xi = set(), 1
        while xi < bound:
            yj = 1
            while xi + yj <= bound:
                ans.add(xi + yj)
                if y == 1:
                    break
                yj *= y
            if x == 1:
                break
            xi *= x
        return list(ans)
