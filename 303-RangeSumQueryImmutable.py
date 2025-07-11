class NumArray:
    numsArray = []
    prefixSums = []

    def __init__(self, nums: List[int]):
        self.numsArray = nums

    def sumRange(self, left: int, right: int) -> int:
        prefixSums = [0] * (right-left + 1)

        for i in range((right-left)+1):
            prefixSums[i] = self.numsArray[left] + prefixSums[i-1]
            left += 1

        return prefixSums[-1]

        