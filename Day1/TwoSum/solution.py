nums = [2,7,11,15]  # Given array
target = 9  # Given target

result = []
for i in range(len(nums)):
    print(i)
    for j in range(i+1, len(nums)):
        print(j)
        if nums[i] + nums[j] == target:
            print(i, j)
            result.append([nums[i], nums[j]])

print(result)
