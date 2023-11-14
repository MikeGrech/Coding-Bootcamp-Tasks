# Integer list
number_list = [8, 3, 5, 1]

# Needed variables
final_number = 0
power_of_ten = 0

# Reversing the order of the number list to make iterating easier
number_list.reverse()



for number in number_list:
    # Adding the next number in the list to the final number
    final_number = final_number + number * 10**power_of_ten

    # Adding a power of ten for the next number
    power_of_ten = power_of_ten + 1


# Printing the number in the list
print(final_number)