def twoSum( nums, target):
        dict = {}
        for i, value in enumerate(nums):
            remain = target - nums[i]

            if remain in dict:
                return [dict[remain], i]

            else:
                dict[value] = i

nums=[2,7,11,10]
target = 9
Result=twoSum(nums,target)
print(Result)