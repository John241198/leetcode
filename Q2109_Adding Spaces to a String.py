s = "LeetcodeHelpsMeLearn"
spaces = [8,13,15]

#initial solution

"""
initially temp as empty list in for loop check the space index reached in if it will add space else it will append in 
temp and return the list as string using join but it doest accept  test case file in time limit exceeded 
"""
temp=[]
for i in range(len(s)):
    if i in spaces:
        temp.append(' '+s[i])
    else:
        temp.append(s[i])
print("".join(temp))

#final solution
"""
repeated same process done for initial solution instant  of list use empty string and add the value 
"""
temp = ""
spaces = set(spaces)
for i in range(len(s)):
    if i in spaces:
        temp += ' ' + s[i]
    else:
        temp += s[i]
        
print(temp)