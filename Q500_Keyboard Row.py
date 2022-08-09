words = ["Hello","Alaska","Dad","Peace"]

#solution
"""
initially result_list is an empty list were in row1 all the alphabets as in keyword as in a set and in row2 and row3 same as row1
in a forloop if a word lower is subset of the row1,row2 and row3 then append the word in result list and finally return the result list
"""
result_list=[]
row1=set('qwertyuiop')
row2=set('asdfghjkl')
row3=set('zxcvbnm')
for word in words:
    if set(word.lower()).issubset(row1) or set(word.lower()).issubset(row2) or set(word.lower()).issubset(row3):
        result_list.append(word)
print(result_list)