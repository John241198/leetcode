import math

s = "foobar"
letter = "o"


#initiall solution

"""
initially b is 0 in for loop s if letter is equal to the character in s and increment if is equal to letter
and finally return the percentage of letter by letter count and length of string divided by 100.
"""
b=0
for i in s:
    if letter == i:
        b+=1
print(round(b*100/len(s)))


#solution
b=0
for i in s:
    if letter == i:
        b+=1
print(math.floor(b*100/len(s)))