class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            if target - nums[i] == nums[i]:
                if d.get(nums[i]) != None:
                    return [d[nums[i]],i]
            d[nums[i]] = i
            
        for key in d.keys():
            if d.get(target - key) != None and target - key != key:
                return [d[key], d[target - key]]
        return [-1,-1]
        
