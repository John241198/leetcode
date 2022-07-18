n=[2,7,11,15]
target = 9

#initial solution

for i in range(len(n)):
    for j in range(i+1, len(n)):
        if n[i] + n[j] == target:
            print(i,j)


#improved solution
result = {}
for i in range(len(n)):
    if target - n[i] not in result:
        result[n[i]] = i
    else:
        print(result[target - n[i]], i)