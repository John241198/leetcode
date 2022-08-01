text = "leetcode"
text = "loonbalxballpoon"

#solution
"""
to find the number of time the letter "balloon" from text has possible
initially d is dictionary which as the letters of balloon as key and values as initially zero
in for loop if the test as this balloon latter it will increment the values in dict and if 
length of text "balloon" less then and letter 'l' and 'o'occurs once it have to return zero
and for key l and o it occur twice so we divide by 2 to be same as other char values in dict 
d and finally return the min value of dict 
"""
d = {'b':0,'a':0,'l':0,'o':0,'n':0}
for item in text:
    if item in ('b','a','l','l','o','o','n'):
        d[item] += 1
if len(d) < 5 or d['l'] == 1 or d['o'] == 1:
    print(0)
d['l'] = int(d['l'] / 2)
d['o'] = int(d['o'] / 2)
result=d.values()
print(result)
print(min(result))


