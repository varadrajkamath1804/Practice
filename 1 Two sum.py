def twoSum(nums, target):

    for i in range(0,len(nums)):
        for j in range(i+1,len(nums)):
            if (nums[i]+ nums[j])==target:
                return "Found:",i,j

        
result = twoSum([1,2,3,4],4)
print(result)
