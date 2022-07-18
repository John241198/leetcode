#initial solution

#nums = [1,1,2]
nums = [0,0,1,1,1,2,2,3,3,4]

result = []
for i in nums:
    if i not in result:
        result.append(i)
nums.clear()
for i in result:
    nums.append(i)
print(len(nums))

#improved solution

k = 0

for n in nums:
    if n != nums[k]:
        k += 1
        nums[k] = n

print(k + 1)