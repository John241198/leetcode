strs = ["flower","flow","flight"]

#initial solution
short=strs[0]
prefix=""
for i in range(len(short)):
    if strs[len(strs)-1][i] == short[i]:
        prefix +=strs[len(strs)-1][i]
    else:
        break
print(prefix)

#improved solution

output = ""
for i in zip(*strs):
    if len(set(i)) == 1:
        output += i[0]
    else:
        break
print(output)
