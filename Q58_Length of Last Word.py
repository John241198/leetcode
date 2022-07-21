s = "   fly me   to   the moon  "

#initial solution
"""
initially declare an empty list as res in for loop split the sentence and append in res using slice find 
the last words and using len function we can find the length of last word.
"""
res = []
for i in s.split():
    res.append(i)
word = res[-1]
length = len(word)
print(length)

#improved solution
ss=s.split()
a=ss[::-1]
print(len(a[0]))
