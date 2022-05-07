#Timestamp 135
import random

random_list = [random.randrange(1,200) for i in range(20)]
print(random_list)

#Get the min, max, the count, and the average of all 20 items, and print them

min_value = random_list[0] #sets the index in random_list to 0, so starting from the first number in random_list
max_value = random_list[0]
item_count = 0
total = 0

for number in random_list:

    #for the sum
    total += number #This is equivalent to total = total + number

    #for the min_value
    #Starting from index 0, if the previous number is greater than the current number, then min_value = current number, so on...
    if min_value > number: #Pointer starts at the first_number (index 0), this line means is first_number greater than second_number
        min_value = number #if previous line is true, then we will set min_value as number

    #for the total number of numbers
    item_count += 1

print("The total of all numbers is " + str(total))
print("The minimum value is " + str(min_value))
print("The total number of numbers in the list is " + str(item_count))


