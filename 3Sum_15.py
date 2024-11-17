class Solution:
    def twoSum(self, numbers, target):
        start = 0
        end = len(numbers) - 1
        res = []
        while start < end:
            if numbers[start] + numbers[end] == target:
                if len(res) == 0 or not (res[-1][0] == numbers[start] and res[-1][1] == numbers[end]):
                    res.append([numbers[start], numbers[end]])
                start += 1
                end -= 1
            elif numbers[start] + numbers[end] < target:
                start += 1
            elif numbers[start] + numbers[end] > target:
                end -= 1
        return [len(res)>0,res]
        
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        prev = 0
        nums.sort()
        for i in range(len(nums)):
            if i == 0 or nums[i] != prev:
                flag, values = self.twoSum(nums[i+1:],0-nums[i])
                if flag:
                    for v in values:
                        result.append([nums[i]]+v)
            prev = nums[i]
        return result

        
