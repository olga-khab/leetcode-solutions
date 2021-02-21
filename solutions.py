class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dct = {}
        for i in range(0,len(nums)):
            dct[nums[i]] = i
        for i in range (0,len(nums)):
            diff = target - nums[i]
            if diff in dct and dct.get(diff) != i:
                return [i,dct.get(diff)]
