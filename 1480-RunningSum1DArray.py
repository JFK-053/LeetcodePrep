class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefixSums = [0] * len(nums)
        for i in range(len(nums)):
            prefixSums[i] = (nums[i] + prefixSums[i -1])

        return prefixSums
        