class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # build this in O(n)
        hashmap = {}
        for index, number in enumerate(nums):
            complement = target - number
            if complement in hashmap: # if we have already seen it, constant time operation O(1)
                return [hashmap[complement], index]
            else:
                hashmap[number] = index
        return
