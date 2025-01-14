nums = input().split(", ")
nums_set = set(x for x in nums)
print(len(nums_set) < len(nums))
