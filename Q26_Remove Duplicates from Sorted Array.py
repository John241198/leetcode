
#nums = [1,1,2]
nums = [0,0,1,1,1,2,2,3,3,4]

#initial solution

"""
Initialize the empty list and in forloop print the nums one by one and in if condition the char or int not in result it will
append in the results after complete have to clear the nums and to append result values in nums as the problem's 
requirement and print the length of nums. 
"""

result = []
for i in nums:
    if i not in result:
        result.append(i)
nums.clear()
for i in result:
    nums.append(i)
print(len(nums))

#improved solution

"""
initialize k = 0 and in forloop check the char is not equal to the nums and increment the k as condition is true
and finally prints the k + 1 to print the length of the removed duplicate length of nums.
"""

k = 0

for n in nums:
    if n != nums[k]:
        k += 1
        
print(k + 1)
