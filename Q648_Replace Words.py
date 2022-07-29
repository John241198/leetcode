dictionary = ["cat","bat","rat"]
sentence = "the cattle was rattled by the battery"

#solution
"""
initially split the sentence and in for loop check the dictionary value is equal to the sentence 
words present in and replace the words in sentence with matched dictionary and return the result 
"""

result = sentence.split(" ")
for i in dictionary:
    for j in range(len(result)):
        if i in result[j][:len(i)]:
            result[j] = i
print(" ".join(result))