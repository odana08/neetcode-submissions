class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i in range(len(nums)):
            difference = target-nums[i]
            if hashmap.get(difference) == None:
                hashmap[nums[i]] = i
            else:
                return [hashmap.get(difference), i]

