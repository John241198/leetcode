words = ["abba","baba","bbaa","cd","cd"]

#initial solution
"""
initially the output list an first element of words and in for loop the len of output last index is 
equal to len of words first index is not equal the append in the output but it was not accepted testcase fail 
"""
output = [words[0]]
for i in range(1, len(words)):
    if len(output[-1]) != len(words[i]):
        output.append(words[i])

print(output)


#final solution
"""
repeating the same process but after the for loop sorting the list1 and list2 from second index in words
and compare the list1 and list2 if is not equal then append in output return the output list.
"""
output = [words[0]]
for i in range(1,len(words)):
    list1="".join(sorted(words[i]))
    list2="".join(sorted(words[i-1]))
    if list1 != list2:
        output.append(words[i])

print(output)