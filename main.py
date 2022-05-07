#even_numbers = list(range(2,11,2))
#print(even_numbers)

#program to count the number of vowels in a sentence using LISTS and IN

my_phrase = "This is a test"
vowel_list = ['a', 'e', 'i', 'o', 'u']
number_vowels = 0

for letters in my_phrase:
    if letters.lower() in vowel_list:
        number_vowels += 1
print (number_vowels)