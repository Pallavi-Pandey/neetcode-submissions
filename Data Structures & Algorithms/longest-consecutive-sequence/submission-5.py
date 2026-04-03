class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        # print(nums)
        longest = 1
        current = 1
        if not nums:
            return 0
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                current += 1
            elif nums[i] != nums[i - 1]:
                longest = max(longest, current)
                current = 1
        longest = max(longest, current)
        # print(longest)
        return longest
        