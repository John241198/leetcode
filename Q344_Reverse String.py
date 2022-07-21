s = ["H", "a", "n", "n", "a", "h"]

#initial solution
"""
initial empty list results and join the s as string and reverse it using slicing
and append the reversed char in result using forloop and clear the s input list
and append the result to s using forloop obtained the expected result as reversed string
in the list
"""
result = []
out = "".join(s)
output = out[::-1]
for i in output:
    result.append(i)
    s.clear()
for i in result:
    s.append(i)

#improved solution
"""
using slice reverse the input list and clear the input string and using extended add the temp list in s
"""

temp = s[::-1]
s.clear()
s.extend(temp)

print(temp)
