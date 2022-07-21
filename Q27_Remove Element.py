nums=[3,2,2,3]
val=2

#initial solution
"""
Initially assigned result is zero in for loop if nums are not equal to
the val then we increment the result and we finally get the output as 
length of nums in result.
"""

result = 0
for n in nums:
    if n is not val:
        result+=1
print(result)




