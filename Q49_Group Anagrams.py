strs = ["eat","tea","tan","ate","nat","bat"]

# initial solution
"""
initially result as empty dictionary in for loop join and sort the word if sorted word is in 
strs then append in result dict as key value else add as key value in dict return the result values as list.
"""
result = {}
for word in strs:
    sortedWord = "".join(sorted(word))
    if sortedWord in result:
        result[sortedWord].append(word)
    else:
        result[sortedWord] = [word]
print(list(result.values()))