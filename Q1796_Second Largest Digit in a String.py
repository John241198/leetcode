s = "dfa12321afd"

#intial solution
"""
initially declare an empty list result in for loop if the char isnumeric() and char not in result 
append in empty list and if len of list is less the 2 return -1 and sort the list to find second 
largest num in the result as output
"""
result = []
for i in s:
    if i.isnumeric() and int(i) not in result:
        result.append(int(i))
if len(result) < 2:
    print(-1)
result.sort(reverse=True)
print(result[1])