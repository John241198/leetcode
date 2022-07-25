words = ["pay","attention","practice","attend"]
pref = "at"

#initial solution
"""
initially count is zero in for loop if i prefix word using slice method i pref is equal to pref 
increment then return count
"""
count = 0
for i in words:
    if i[:len(pref)] == pref:
        count += 1
print(count)