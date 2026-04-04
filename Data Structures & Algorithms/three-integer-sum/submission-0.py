class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            # skip duplicate 'a'
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            a = nums[i]
            l, r = i + 1, len(nums) - 1

            while l < r:
                s = a + nums[l] + nums[r]

                if s > 0:
                    r -= 1
                elif s < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1

                    # skip duplicates for l
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

        return res