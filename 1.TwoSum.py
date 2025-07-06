class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = []
        indices = {}
        for i in range(len(nums)):
            indices[nums[i]] = indices.get(nums[i], [])
            indices[nums[i]].append(i)
        
        for num in nums:
            remainder = target-num
            if remainder in indices:
                if (remainder == num) and (len(indices[remainder]) > 1) :
                    output.append(indices[num][0])
                    output.append(indices[num][1])
                    return output
                elif remainder != num:
                    output.append(indices[num][0])
                    output.append(indices[remainder][0])
                    return output
        