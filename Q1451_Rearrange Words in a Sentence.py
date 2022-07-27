text = "Leetcode is cool"

#initial solution

"""
in result_txt using lower inbuilt method charge the words in the string lower and split it as list 
and again sort the list with length of words in ascending order and the sentence must start with
title case so we use upper method and finally return the result text by join the string 
"""
result_txt = text.lower().split(' ')
result_txt = sorted(result_txt, key=len)
result_txt[0] = result_txt[0][0].upper() + result_txt[0][1:]
print(' '.join(result_txt))