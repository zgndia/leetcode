class Solution(object):
    def twoSum(self, nums, target):
        pos = 0
        for number in nums:
            for i in range(len(nums)):
                if pos == i:
                    continue
                if number + nums[i] == target:
                    return [pos, i]
            pos += 1