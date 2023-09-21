#Write a program to sort a string according to the frequency of character and return the final string.
#Input: "tree"          
#Output: "eert" 
def sortString(s):
    dict = {}
    for i in s:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    res = ""
    for i in sorted(dict.items(), key=lambda x: x[1], reverse=True):
        res += i[0] * i[1]
    return res

s = input()
print(sortString(s))



