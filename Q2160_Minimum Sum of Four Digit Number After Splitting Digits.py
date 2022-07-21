
num = 2932

#intital solution

"""
Initially convert the num to string and sort the string and using slicing alternate number to new number's and convert
into integer and add the both integer.
"""

s = str(num)
s = "".join(sorted(s))
new1 = s[0] + s[2]
new2 = s[1] + s[3]

print(int(new1) + int(new2))

#improved solution
"""
initially num_list as empty list in while loop if num greater then 0 we
append the num by modulus operator by 10 to get last digit and append in
num_list as remainder and then using floor division we can remove the append 
num in num and continue the appending reaming nums and sorted the list and 
added in digits in separate variable and we add digits alternatively. 
"""

num_list = []
while num > 0:
    num_list.append(num % 10)
    num = num // 10

n1, n2, n3, n4 = sorted(num_list)

print(10 * n1 + n3 + 10 * n2 + n4)



