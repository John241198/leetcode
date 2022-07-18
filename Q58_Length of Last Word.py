s = "   fly me   to   the moon  "

#initial solution
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