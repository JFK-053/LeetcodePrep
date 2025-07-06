class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        sortedCounts = {i:v for i, v in sorted(counts.items(), key = lambda item:item[1], reverse = True)}

        sortedKeys =  list(sortedCounts.keys())
        return sortedKeys[:k]