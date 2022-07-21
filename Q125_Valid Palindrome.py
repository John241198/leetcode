s ="race a car"

#initial solution
"""
In the first forloop append the character in out empty list using lower method and in second
for loop validate the non-alphanumeric character in char and compare and remove in out
and in if condition input is equal to reverse string then its true else it false.
"""
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
"""
using lower method convert the string to lower and in char it as all alphabet and nums as testcase contains
compare it with forloop with s and char if it as it will append string list and we can join the string to remove
white space and using if condition input is equal to reverse string then its true else false.
"""
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
