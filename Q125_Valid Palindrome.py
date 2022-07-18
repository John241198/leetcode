s ="race a car"

#initial solution
out=[]
char=[',',':']
for i in s:
    out.append(i.lower())
    for i in char:
        while i in out:
            out.remove(i)

x=''.join(out)
final=x.replace(' ','')
if final == final[::-1]:
    print("true")
else:
    print("false")


#improved solution

s = s.lower()
char = 'abcdefghijklmnopqrstuvwxyz0123456789'
string = []
for i in s:
    if i in char:
        string.append(i)

output = ''.join(string)

if output == output[::-1]:
    print("true")
else:
    print("false")