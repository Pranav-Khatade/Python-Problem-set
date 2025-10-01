#maximum subarray problem

nums = [-4,-5,-1,0,2,5,7]
maxim = nums[0]
maxin = nums[0]
for num in nums:
	maxim = max(num, maxim+num)
	maxin = max(maxin, maxim)

print(maxin)