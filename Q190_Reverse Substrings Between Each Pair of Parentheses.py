s = "(abcd)"
#s = "(u(love)i)"
#s = "(ed(et(oc))el)"

#solution
"""
intially s as list of input string to reverse and s1 as empty list in while loop s pop the first element in s
and if a is not equal to ')' append the char in s1 else s2 as empty list again while loop as true
pop s1 last element on list s1 if x is equal to '(' it will add the s2 to s1 empty list and finally
return the s1 using join method 
"""

s = list(s)
s1 = []
while s:
    a = s.pop(0)
    if a != ')':
        s1.append(a)
    else:
        s2 = []
        while True:
            x = s1.pop()
            if x == '(':
                s1 += s2
                break
            else:
                s2.append(x)
print(''.join(s1))