nums=[3,2,2,3]
val=2

#initial solution

result = 0
for n in nums:
    if n is not val:
        nums[result] = n
        result+=1
print(result)


#improved solution

