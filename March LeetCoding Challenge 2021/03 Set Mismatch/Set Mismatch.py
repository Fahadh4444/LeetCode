class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        realSum = sum(nums)
        setSum = sum(set(nums))
        repeatedNum = realSum - setSum
        missingNum = sum(range(1, len(nums)+1)) - setSum
        return [repeatedNum, missingNum]
