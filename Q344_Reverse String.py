s = ["H", "a", "n", "n", "a", "h"]

#initial solution
"""
result = []
out = "".join(s)
output = out[::-1]
for i in output:
    result.append(i)
    s.clear()
for i in result:
    s.append(i)
"""
#improved solution
temp = s[::-1]
s.clear()
s.extend(temp)

print(temp)