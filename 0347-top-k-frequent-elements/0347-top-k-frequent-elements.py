class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        itemDict = {}
        
        for i in nums:
            if i in itemDict:
                itemDict[i] += 1
            else:
                itemDict[i] = 1
        
        return sorted(itemDict, key=itemDict.get, reverse=True)[:k]
        