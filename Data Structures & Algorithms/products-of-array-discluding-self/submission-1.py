class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        op = []
        prefix = 1
        for i in nums:
            op.append(prefix)
            prefix = prefix*i

        suffix = 1
        for i in range(len(nums)-1,-1,-1):
            op[i] = op[i]*suffix
            suffix = suffix*nums[i]
        return op


