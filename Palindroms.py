#Challenge: come up with an algorithm that can tell is a word is a palindrom or not
#Palindroms are words that are spelled the same backwards and forwards

string_1 = "mom"

#Method 1: start with two loops and check the beginning letter with the end each time


#Method 2: using rev

rev = string_1[::-1]
if rev == string_1:
    print(string_1 + " " + "is a palindrom")
else:
    print(string_1 + " " + "is not a palindrom")



