people = [3,2,2,1]
limit = 3

#initial solution

"""
sort the input list people then initialize output as zero and in while length of people is true the
increment the output in first if length of people is equal to 1 then break the while loop
then second if the index of first element and last element sum is less then and equal to limit the
pop the first element and out of if pop last element and finally return the output.
"""

people.sort()
output = 0
while(len(people)):
    output += 1
    if(len(people) == 1):
        break
    if(people[0] + people[-1] <=  limit):
        people.pop(0)
    people.pop()
print(output)