class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        realSum = sum(nums)
        totalSum = sum(range(1, len(nums)+1))
        return totalSum-realSum
