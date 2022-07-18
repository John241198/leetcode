s = "abcd"
t = "abcde"

#initial solution
for i in range(len(s)):
    if s[i] != t[i]:
        print(t[i])
print(t[-1])


#improved solution

strs = sorted(s)
strt = sorted(t)
for i in range(len(strs)):
    if strs[i] != strt[i]:
        print(strt[i])
print(strt[-1])