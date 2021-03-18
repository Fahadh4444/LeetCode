class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        up, down = 1, 1
        for i in range(n-1):
            if(nums[i] - nums[i+1] > 0):
                down = up + 1
            if(nums[i] - nums[i+1] < 0):
                up = down + 1
        return max(up, down)
