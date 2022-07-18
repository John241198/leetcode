n=[2,7,11,15]
target = 9

#initial solution

"""At first forloop it will start to print the index of element in n and second forloop it start print
index of second element and compare using if condition by add elemnt first and second is equal to
target it print its index as output"""

for i in range(len(n)):
    for j in range(i+1, len(n)):
        if n[i] + n[j] == target:
            print(i,j)


#improved solution
""" In a first forloop it prints the index position of a element in a list n.And in if condition target is sub
with every element in n if not in intially declared dictinory result it appends in results both element and its index
else it prints its indexposition of the result and n"""

result = {}
for i in range(len(n)):
    if target - n[i] not in result:
        result[n[i]] = i
    else:
        print(result[target - n[i]], i)
