
num = 2932

#intital solution
s = str(num)
s = "".join(sorted(s))
new1 = s[0] + s[2]
new2 = s[1] + s[3]

print(int(new1) + int(new2))

#improved solution
num_list = []
while num > 0:
    num_list.append(num % 10)
    num = num // 10

n1, n2, n3, n4 = sorted(num_list)

print(10 * n1 + n3 + 10 * n2 + n4)



