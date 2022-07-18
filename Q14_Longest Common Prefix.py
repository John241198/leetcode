strs = ["flower","flow","flight"]

#initial solution

"""initialize the short as strs first element and prefix as an empty string and in forloop print
 the index of every character in short and compare with the strs elements character with short char as follows
and append the same char in prefix and print the prefix at the end of the forloop"""

short=strs[0]
prefix=""
for i in range(len(short)):
    if strs[len(strs)-1][i] == short[i]:
        prefix +=strs[len(strs)-1][i]
    else:
        break
print(prefix)

#improved solution

"""
Initialize the output as empty string to append the similar char in forloop using zip function
it will zip the char by char for first char in every words in a list and using if condition convert the char as set and length is equal to 
1 then it will add the char in output and finally return the similar char in output 
"""

output = ""
for i in zip(*strs):
    if len(set(i)) == 1:
        output += i[0]
    else:
        break
print(output)
