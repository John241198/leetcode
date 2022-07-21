"""
initially split the sentence and in for loop we extract the last integer and  words to append
in dict and sort the dict based on key and append the words on result based on sorting.
"""

s = "is2 sentence4 This1 a3"

x = s.split()
dic = {}
for i in x:
    dic[i[-1]] = i[:-1]

result=[]
for i in sorted(dic):
    result.append(dic[i])

print(' '.join(result))


