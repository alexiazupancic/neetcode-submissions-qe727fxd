class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range (0, len(nums)):
            difference = target - nums[i]
            if difference in nums:
                return [i, nums.index(difference)]
