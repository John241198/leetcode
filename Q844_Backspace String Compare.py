#s = "ab#c"
#t = "ad#c"
s = "ab##"
t = "c#d#"

#solution

"""
initially s_str and t_str is empty string in forloop if the s char's is equal to '#' it will replace s_str into first char
else it will add char in s_str same as for t_str and finally compare the s_str and t_str is equal 
"""
s_str = ""
t_str = ""
for i in range(len(s)):
    if s[i] == '#':
        s_str = s_str[:-1]
    else:
        s_str += s[i]
for i in range(len(t)):
    if t[i] == '#':
        t_str = t_str[:-1]
    else:
        t_str += t[i]

print(s_str == t_str)